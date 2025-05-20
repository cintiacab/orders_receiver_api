from src.models.repositories.interface.user_repository import UserRepositoryInterface
from .interfaces.list_users import ListUserInteface

class ListUser(ListUserInteface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def list_all(self) -> list:
        users = self.__get_users()
        return self.__format_response(users)

    def __get_users(self) -> tuple:
        users = self.__user_repository.list_users()
        return users
    
    def __format_response(self, users: tuple):
        formatted_response = []
        for user in users:
            formatted_response.append({
                "id": user[0],
                "username": user[1],
            })
        return {
            "data":{
                "type" : "users",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
