from src.models.repositories.interface.order_repository import OrderRepositoryInterface
from src.models.repositories.interface.user_repository import UserRepositoryInterface
from .interfaces.order_register import OrderRegisterInterface
from src.errors.errors_types.http_not_found_error import HttpNotFound

class OrderRegister(OrderRegisterInterface):
    def __init__(self, order_repository: OrderRepositoryInterface, user_repository: UserRepositoryInterface) -> None:
        self.__order_repository = order_repository
        self.__user_repository = user_repository

    def registry(self, user_id: int, description: str) -> dict:
        self.__validate_user(user_id)
        self.__register_new_order(description, user_id)
        return self.__format_response(description)
        
    def __validate_user(self, user_id: str) -> None:
        user = self.__user_repository.get_user_by_id(user_id)
        if not user:
            raise HttpNotFound("User not found")

    def __register_new_order(self, description: str, user_id: int) -> None:
        self.__order_repository.order_registry(description, user_id)

    def __format_response(self, description: str) -> dict:
        return{
            "data": {
                "type": "order",
                "count": 1,
                "description": description
            }
        }