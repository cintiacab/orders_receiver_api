from abc import ABC, abstractmethod

class OrderRepositoryInterface(ABC):

    @abstractmethod
    def registry_order(self, description: str, user_id: int) -> dict: pass

    @abstractmethod
    def list_orders(self, user_id: int) -> list: pass
