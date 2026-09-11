"""Couche d'accès aux données — volontairement isolée du reste du backend.

Environnement de preview Emergent : MongoDB (motor).
Migration production : remplacer UNIQUEMENT ce module par un adaptateur
MariaDB (table `leads`, requêtes préparées — voir README.md, section
« Migration MariaDB »). Aucune autre partie du code ne dépend de MongoDB.
"""
import os

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

_client = AsyncIOMotorClient(os.environ["MONGO_URL"])
_db = _client[os.environ["DB_NAME"]]

LEADS_COLLECTION = "leads"


class LeadStore:
    """Accès aux demandes de contact (leads)."""

    async def insert(self, lead: dict) -> str:
        result = await _db[LEADS_COLLECTION].insert_one(dict(lead))
        return str(result.inserted_id)

    async def set_email_status(self, lead_id: str, status: str, sent_at=None) -> None:
        await _db[LEADS_COLLECTION].update_one(
            {"_id": ObjectId(lead_id)},
            {"$set": {"email_status": status, "email_sent_at": sent_at}},
        )

    async def count(self) -> int:
        return await _db[LEADS_COLLECTION].count_documents({})


lead_store = LeadStore()
