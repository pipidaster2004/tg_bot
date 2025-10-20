from bot.handlers.handler import Handler, HandlerStatus
from bot.telegram_client import sendMessage

class MessageTextEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "text" in update["message"]

    def handle(self, update:dict):
        sendMessage(chat_id = update["message"]["chat"]["id"],
                    text = update["message"]["text"],)
        print(f"send message: {update["message"]["text"]}")
        return HandlerStatus.STOP