from abc import ABC, abstractmethod

class LoginEnablerInterface(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> dict: pass
