"""Envoi d'e-mails via l'interface locale sendmail/Exim en production."""

import os
import re
import subprocess
from email.message import EmailMessage
from email.utils import formatdate

SUBJECT = "Nouvelle demande de contact — Allo Bris de Glace"

FIELD_LABELS = [
    ("nom", "Nom"),
    ("prenom", "Prénom"),
    ("telephone", "Téléphone"),
    ("email", "E-mail"),
    ("region", "Région"),
    ("type_vehicule", "Type de véhicule"),
    ("immatriculation", "Immatriculation"),
    ("service", "Service demandé"),
    ("message", "Message"),
    ("created_at", "Date de demande"),
    ("page_source", "Page source"),
]


def _sanitize(value) -> str:
    """Neutralise les caractères de contrôle."""
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(value or ""))
    return text.strip()


def _header_safe(value) -> str:
    return re.sub(r"[\r\n]+", " ", _sanitize(value))


def send_lead_email(lead: dict):
    """Envoie le message via Exim local et retourne (True, None) ou (False, erreur)."""
    mail_from = os.environ.get("MAIL_FROM", "").strip()
    mail_to = os.environ.get("MAIL_TO", "").strip()

    if not mail_from or not mail_to:
        return False, "MAIL_FROM ou MAIL_TO non configuré"

    lines = [
        "Nouvelle demande de contact reçue depuis le site allobrisdeglace.com",
        "",
    ]

    for key, label in FIELD_LABELS:
        lines.append(f"{label} : {_sanitize(lead.get(key, '')) or '—'}")

    body = "\n".join(lines) + "\n"

    message = EmailMessage()
    message["Subject"] = SUBJECT
    message["From"] = _header_safe(mail_from)
    message["To"] = _header_safe(mail_to)
    message["Date"] = formatdate(localtime=True)
    message.set_content(body, subtype="plain", charset="utf-8")

    sendmail_path = "/usr/sbin/sendmail"

    if not os.path.isfile(sendmail_path):
        return False, f"{sendmail_path} introuvable"

    try:
        result = subprocess.run(
            [sendmail_path, "-t", "-i"],
            input=message.as_string(),
            text=True,
            capture_output=True,
            timeout=15,
            check=False,
        )

        if result.returncode != 0:
            error = (result.stderr or result.stdout or "").strip()
            return False, error or f"sendmail exited with code {result.returncode}"

        return True, None

    except Exception as exc:
        return False, str(exc)
