from abc import ABC, abstractmethod

class OrderRepositoryInterface(ABC):

    @abstractmethod
    def order_registry(self, description: str, user_id: int) -> dict: pass

    @abstractmethod
    def list_orders(self, user_id: int) -> list: pass
