from bot.database_client import persist_updates
from bot.handler import Handler


class DatabaseLogger(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update
    
    def handle(self, update:dict) -> bool:
        persist_updates(update)
        return True