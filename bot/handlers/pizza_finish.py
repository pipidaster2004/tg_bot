import json
from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
import bot.telegram_client
import bot.database_client
from bot.handlers.handler import Handler, HandlerStatus


class PizzaFinish(Handler):
    def can_handle(
            self,
            update: dict,
            state: str,
            order_json: dict,
            storage: Storage,
            messenger: Messenger,
        ):
        if "callback_query" not in update:
            return False

        if state != "WHAIT_FOR_APROVE":
            return False

        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("order_")

    def handle(
            self,
            update: dict,
            state: str,
            order_json: dict,
            storage: Storage,
            messenger: Messenger,
        ):
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        order_mapping = {
            "order_confirm": "Confrim",
            "order_again": "Again",
        }

        order_type = order_mapping.get(callback_data)
        messenger.answerCallbackQuery(update["callback_query"]["id"])
        messenger.deleteMessage(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            message_id=update["callback_query"]["message"]["message_id"],
        )
        new_order_json = storage.get_user_order(telegram_id)
        if new_order_json:
            order_text = f"Your order confrimed:\nPizza: {new_order_json['pizza_name']}\nSize: {new_order_json['pizza_size']}\nDrink: {new_order_json['drink']}"
        else:
            order_text = "No order found"
        if order_type == "Confrim":
            storage.update_user_state(telegram_id, "ORDER_FINISHED")
            messenger.sendMessage(
                chat_id=update["callback_query"]["message"]["chat"]["id"],
                text=order_text,
            )
        elif order_type == "Again":
            storage.update_user_state(telegram_id, "WHAIT_FOR_PIZZA_NAME")
            messenger.sendMessage(
                chat_id=update["callback_query"]["message"]["chat"]["id"],
                text="Please choose pizza name",
                reply_markup=json.dumps(
                    {
                        "inline_keyboard": [
                            [
                                {
                                    "text": "Margarita",
                                    "callback_data": "pizza_margarita",
                                },
                                {
                                    "text": "Pepperoni",
                                    "callback_data": "pizza_pepperoni",
                                },
                            ],
                            [
                                {"text": "Bavarian", "callback_data": "pizza_bavarian"},
                                {"text": "Devils", "callback_data": "pizza_devils"},
                            ],
                        ]
                    }
                ),
            )
        return HandlerStatus.STOP
