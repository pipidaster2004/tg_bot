import time
import bot.telegram_client
import bot.database_client

def main()->None:
    next_update_offset = 0
    try:
        while True:
            updates = bot.telegram_client.getUpdates(next_update_offset)
            bot.database_client.persist_updates(updates)
            for update in updates:
                bot.telegram_client.sendMessage(
                    chat_id = update["message"]["chat"]["id"],
                    text = update["message"]["text"],
                )
                print(".", end="", flush=True)
                next_update_offset = max(next_update_offset, update["update_id"] + 1)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()