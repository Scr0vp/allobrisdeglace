"""Envoi d'e-mails via le serveur SMTP local (Exim en production).

Configuration exclusivement par variables d'environnement :
SMTP_HOST, SMTP_PORT, SMTP_SECURE, SMTP_USER, SMTP_PASSWORD, MAIL_FROM, MAIL_TO.
Aucune donnée SMTP n'est exposée au frontend.
"""
import os
import re
import smtplib
from email.message import EmailMessage
from email.utils import formatdate

SUBJECT = "Nouvelle demande de contact — Allo Brise de Glace"

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
    """Neutralise les injections d'en-têtes et caractères de contrôle."""
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(value or ""))
    return text.strip()


def _header_safe(value) -> str:
    return re.sub(r"[\r\n]+", " ", _sanitize(value))


def send_lead_email(lead: dict):
    """Retourne (True, None) en cas de succès, (False, erreur) sinon."""
    mail_from = os.environ.get("MAIL_FROM", "").strip()
    mail_to = os.environ.get("MAIL_TO", "").strip()
    if not mail_from or not mail_to:
        return False, "MAIL_FROM ou MAIL_TO non configuré"

    host = os.environ.get("SMTP_HOST", "127.0.0.1")
    port = int(os.environ.get("SMTP_PORT", "25"))

    lines = ["Nouvelle demande de contact reçue depuis le site allobrisdeglace.com", ""]
    for key, label in FIELD_LABELS:
        lines.append(f"{label} : {_sanitize(lead.get(key, '')) or '—'}")
    body = "\n".join(lines) + "\n"

    message = EmailMessage()
    message["Subject"] = SUBJECT
    message["From"] = _header_safe(mail_from)
    message["To"] = _header_safe(mail_to)
    message["Date"] = formatdate(localtime=True)
    message.set_content(body, subtype="plain", charset="utf-8")

    try:
        with smtplib.SMTP(host, port, timeout=10) as smtp:
            if os.environ.get("SMTP_SECURE", "false").lower() == "true":
                smtp.starttls()
            smtp_user = os.environ.get("SMTP_USER", "").strip()
            if smtp_user:
                smtp.login(smtp_user, os.environ.get("SMTP_PASSWORD", ""))
            smtp.send_message(message)
        return True, None
    except Exception as exc:  # l'erreur est journalisée par l'appelant
        return False, str(exc)
