from bot.handler import Handler
from bot.telegram_client import sendPhoto


class MessagePhotoEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]

    def handle(self, update:dict) -> bool:
        photos = update["message"]["photo"]
        if photos:
            largest_photo = photos[-1]
            file_id = largest_photo["file_id"]
            sendPhoto(
                chat_id=update["message"]["chat"]["id"],
                photo=file_id 
            )
            print(f"Sent photo with file_id: {file_id}")
        
        return False