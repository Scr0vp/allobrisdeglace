"""API backend — ALLO BRISE DE GLACE.

Endpoints :
- GET  /api/health   : contrôle de santé
- GET  /api/config   : identifiants de suivi publics (Google Ads / Analytics)
- POST /api/contact  : réception du formulaire de contact (lead)
"""
import asyncio
import logging
import os
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

from database import lead_store  # noqa: E402  (import après load_dotenv)
from mailer import send_lead_email  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("allobrisdeglace")

app = FastAPI(title="ALLO BRISE DE GLACE — API", docs_url=None, redoc_url=None)
api_router = APIRouter(prefix="/api")

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PHONE_RE = re.compile(r"^\+?[0-9][0-9 .\-()]{7,18}$")

REGIONS = [
    "Île-de-France", "Nord-Ouest", "Nord-Est", "Sud-Ouest", "Sud-Est",
    "Genève", "Montréal", "Belgique", "Autre",
]
SERVICES = [
    "Remplacement de pare-brise",
    "Réparation d'impact",
    "Remplacement de vitre latérale",
    "Remplacement de lunette arrière",
    "Autre",
]

MSG_REQUIRED = "Ce champ est obligatoire."
MSG_EMAIL = "Veuillez saisir une adresse e-mail valide."
MSG_PHONE = "Veuillez saisir un numéro de téléphone valide."
MSG_INVALID = "Veuillez vérifier les informations saisies."
MSG_SUCCESS = "Votre demande a bien été envoyée. Nous vous recontacterons dans les meilleurs délais."
MSG_TOO_MANY = "Trop de demandes. Veuillez réessayer dans quelques minutes."
MSG_ERROR = "Une erreur est survenue. Veuillez réessayer ou nous appeler directement."

RATE_LIMIT = 5
RATE_WINDOW_SECONDS = 600
_requests_log = defaultdict(list)


def _is_rate_limited(ip: str) -> bool:
    now = time.time()
    entries = [t for t in _requests_log[ip] if now - t < RATE_WINDOW_SECONDS]
    if len(entries) >= RATE_LIMIT:
        _requests_log[ip] = entries
        return True
    entries.append(now)
    _requests_log[ip] = entries
    return False


class ContactPayload(BaseModel):
    nom: str = ""
    prenom: str = ""
    telephone: str = ""
    email: str = ""
    region: str = ""
    type_vehicule: str = ""
    immatriculation: str = ""
    service: str = ""
    message: str = ""
    consentement_rgpd: bool = False
    page_source: str = ""
    entreprise: str = ""  # champ anti-spam (honeypot)


@api_router.get("/health")
async def health():
    return {"status": "ok"}


@api_router.get("/config")
async def public_config():
    return {
        "google_ads_conversion_id": os.environ.get("GOOGLE_ADS_CONVERSION_ID", ""),
        "google_ads_conversion_label": os.environ.get("GOOGLE_ADS_CONVERSION_LABEL", ""),
        "google_analytics_id": os.environ.get("GOOGLE_ANALYTICS_ID", ""),
    }


@api_router.post("/contact")
async def submit_contact(payload: ContactPayload, request: Request):
    client_ip = request.client.host if request.client else "inconnue"

    if payload.entreprise.strip():
        logger.info("Honeypot déclenché (IP %s) — soumission ignorée", client_ip)
        return {"ok": True, "message": MSG_SUCCESS}

    if _is_rate_limited(client_ip):
        return JSONResponse(status_code=429, content={"ok": False, "message": MSG_TOO_MANY})

    errors = {}
    if not payload.nom.strip():
        errors["nom"] = MSG_REQUIRED
    if not payload.prenom.strip():
        errors["prenom"] = MSG_REQUIRED
    if not payload.telephone.strip():
        errors["telephone"] = MSG_REQUIRED
    elif not PHONE_RE.match(payload.telephone.strip()):
        errors["telephone"] = MSG_PHONE
    if not payload.email.strip():
        errors["email"] = MSG_REQUIRED
    elif not EMAIL_RE.match(payload.email.strip()):
        errors["email"] = MSG_EMAIL
    if payload.region.strip() not in REGIONS:
        errors["region"] = MSG_REQUIRED
    if not payload.type_vehicule.strip():
        errors["type_vehicule"] = MSG_REQUIRED
    if payload.service.strip() not in SERVICES:
        errors["service"] = MSG_REQUIRED
    if not payload.message.strip():
        errors["message"] = MSG_REQUIRED
    if not payload.consentement_rgpd:
        errors["consentement_rgpd"] = MSG_REQUIRED

    if errors:
        return JSONResponse(
            status_code=400,
            content={"ok": False, "message": MSG_INVALID, "errors": errors},
        )

    lead = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "nom": payload.nom.strip(),
        "prenom": payload.prenom.strip(),
        "telephone": payload.telephone.strip(),
        "email": payload.email.strip(),
        "region": payload.region.strip(),
        "type_vehicule": payload.type_vehicule.strip(),
        "immatriculation": payload.immatriculation.strip(),
        "service": payload.service.strip(),
        "message": payload.message.strip(),
        "consentement_rgpd": True,
        "page_source": payload.page_source.strip()[:500],
        "ip_address": client_ip,
        "user_agent": request.headers.get("user-agent", "")[:300],
        "email_status": "pending",
        "email_sent_at": None,
    }

    try:
        lead_id = await lead_store.insert(lead)
        logger.info("Lead enregistré (%s) — région %s", lead_id, lead["region"])
    except Exception:
        logger.exception("Échec d'enregistrement du lead en base")
        return JSONResponse(status_code=500, content={"ok": False, "message": MSG_ERROR})

    sent, error = await asyncio.to_thread(send_lead_email, lead)
    if sent:
        await lead_store.set_email_status(
            lead_id, "sent", datetime.now(timezone.utc).isoformat()
        )
        logger.info("E-mail envoyé pour le lead %s", lead_id)
    else:
        await lead_store.set_email_status(lead_id, "failed")
        logger.error("Échec d'envoi d'e-mail pour le lead %s : %s", lead_id, error)

    return {"ok": True, "message": MSG_SUCCESS}


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Cache-Control", "no-store")
    return response


@app.on_event("startup")
async def on_startup():
    logger.info("Démarrage de l'application ALLO BRISE DE GLACE")
    try:
        count = await lead_store.count()
        logger.info("Connexion à la base de données établie (%s leads)", count)
    except Exception:
        logger.exception("Connexion à la base de données impossible")
