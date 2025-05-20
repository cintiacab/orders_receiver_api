from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def user_registry(self, username: str, password: str) -> None: pass

    @abstractmethod
    def list_users(self) -> list: pass

    @abstractmethod
    def get_user_by_username(self, username:str) -> tuple[int, str, str]: pass
