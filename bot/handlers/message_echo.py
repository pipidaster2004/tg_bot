from bot.handler import Handler
from bot.telegram_client import sendMessage

class MessageEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "text" in update["message"]

    def handle(self, update:dict) -> bool:
        sendMessage(chat_id = update["message"]["chat"]["id"],
                    text = update["message"]["text"],)
        return False