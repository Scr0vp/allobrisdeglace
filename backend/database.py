"""Couche d'accès aux données MariaDB pour les leads.

Le frontend/API ne dépend pas du moteur SQL directement : toute la persistance
passe par LeadStore. La base utilisée en production est MariaDB.
"""
import asyncio
import os
from datetime import datetime

import aiomysql


DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "127.0.0.1"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "user": os.environ.get("DB_USER", ""),
    "password": os.environ.get("DB_PASSWORD", ""),
    "db": os.environ.get("DB_NAME", "allobrisdeglace"),
    "charset": "utf8mb4",
    "autocommit": True,
}


def _db_datetime(value):
    """Convert an ISO timestamp to a naive UTC datetime for MariaDB."""
    if value is None:
        return None
    if isinstance(value, datetime):
        if value.tzinfo:
            return value.astimezone().replace(tzinfo=None)
        return value
    text = str(value).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo:
        parsed = parsed.astimezone().replace(tzinfo=None)
    return parsed


class LeadStore:
    """Accès aux demandes de contact (table MariaDB `leads`)."""

    async def insert(self, lead: dict) -> int:
        created_at = _db_datetime(lead.get("created_at")) or datetime.utcnow()
        query = """
            INSERT INTO leads (
                created_at, nom, prenom, telephone, email, region,
                type_vehicule, immatriculation, service, message,
                consentement_rgpd, page_source, ip_address, user_agent,
                email_status, email_sent_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s)
        """
        params = (
            created_at,
            lead.get("nom", ""),
            lead.get("prenom", ""),
            lead.get("telephone", ""),
            lead.get("email", ""),
            lead.get("region", ""),
            lead.get("type_vehicule", ""),
            lead.get("immatriculation") or None,
            lead.get("service", ""),
            lead.get("message", ""),
            1 if lead.get("consentement_rgpd") else 0,
            lead.get("page_source") or None,
            lead.get("ip_address") or None,
            lead.get("user_agent") or None,
            lead.get("email_status", "pending"),
            _db_datetime(lead.get("email_sent_at")),
        )

        async with await aiomysql.connect(**DB_CONFIG) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, params)
                return int(cursor.lastrowid)

    async def set_email_status(self, lead_id: int, status: str, sent_at=None) -> None:
        query = "UPDATE leads SET email_status=%s, email_sent_at=%s WHERE id=%s"
        async with await aiomysql.connect(**DB_CONFIG) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, (status, _db_datetime(sent_at), int(lead_id)))

    async def count(self) -> int:
        async with await aiomysql.connect(**DB_CONFIG) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT COUNT(*) FROM leads")
                row = await cursor.fetchone()
                return int(row[0] if row else 0)


lead_store = LeadStore()
