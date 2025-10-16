from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def can_handle(self, update: dict) -> bool:
        pass

    @abstractmethod
    def handle(self, update:dict) -> bool:
        """
        return: -true:  signal for dispatcher to continue processing
                -fasle: signal for dispatcher to stop processing
        """
        pass