from abc import ABC, abstractmethod

class ListUserInteface(ABC):

    @abstractmethod
    def list_all(self) -> dict: pass
