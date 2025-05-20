from abc import ABC, abstractmethod

class ListOrdersInteface(ABC):
   
    @abstractmethod
    def list_orders(self, user_id: int) -> dict: pass
