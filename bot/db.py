from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from config import mongodb_settings


client = AsyncIOMotorClient(mongodb_settings.url)
db = client.get_database(mongodb_settings.NAME)
payments_collection = db.get_collection(mongodb_settings.COLLECTION)
