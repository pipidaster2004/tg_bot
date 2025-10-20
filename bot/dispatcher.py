from bot.handlers.handler import Handler, HandlerStatus

class Dispatcher:
    def __init__(self):
        self._handlers: list[Handler] = []

    def add_handlers(self, *handlers: list[Handler]) -> None:
        for handler in handlers:
            self._handlers.append(handler)
            print(f"add handler {str(handler)}")

    def dispatch(self, update: dict) -> None:
        for handler in self._handlers:
            if handler.can_handle(update):
                signal = handler.handle(update)
                if signal == HandlerStatus.STOP: break
