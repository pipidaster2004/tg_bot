import time
import bot.telegram_client
import bot.database_client

def main()->None:
    next_update_offset = 0
    while True:
        updates = bot.telegram_client.getUpdates(next_update_offset)
        bot.database_client.persist_updates(updates)
        for update in updates:
            bot.telegram_client.sendMessage(
                chat_id = update["message"]["chat"]["id"],
                text = update["message"]["text"],
            )
        print(".", end="", flush=True)
        time.sleep(1)
        next_update_offset = max(next_update_id, update["update_id"])
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()