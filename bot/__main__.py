from bot.dispatcher import Dispatcher
from bot.handlers.database_logger import DatabaseLogger
from bot.handlers.message_photo_echo import MessagePhotoEcho
from bot.handlers.message_text_echo import MessageTextEcho
from bot.long_polling import start_long_polling

def main()->None:
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handlers(
                                DatabaseLogger(), 
                                MessageTextEcho(),
                                MessagePhotoEcho(),
                               )
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()