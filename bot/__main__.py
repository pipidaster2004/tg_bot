from bot.dispatcher import Dispatcher
from bot.handlers.message_echo import MessageEcho
from bot.long_polling import start_long_polling

def main()->None:
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(MessageEcho())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()