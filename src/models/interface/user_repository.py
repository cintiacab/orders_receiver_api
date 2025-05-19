from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def user_registry(self, username: str, password: str) -> None: pass

    @abstractmethod
    def list_users(self) -> list: pass
