from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def registry_user(self, username: str, password: str) -> dict: pass

    @abstractmethod
    def list_users(self) -> list: pass
