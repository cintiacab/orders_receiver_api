from src.models.repositories.interface.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JwtHandler
from .interfaces.login_enabler import LoginEnablerInterface
from src.errors.errors_types.http_not_found_error import HttpNotFound
from src.errors.errors_types.http_bad_request_error import HttpBadRequest

class LoginEnabler(LoginEnablerInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()
        self.__jwt_handler = JwtHandler()

    def login(self, username: str, password: str) -> dict:
        user = self.__get_user(username)
        user_id = user[0]
        username = user[1]
        hashed_password = user[2]
        self.__check_password(password, hashed_password)
        token = self.__create_token(user_id, username)
        return self.__format_response(username, token)

    def __get_user(self, username: str) -> tuple:
        user = self.__user_repository.get_user_by_username(username)
        if not user: 
            raise HttpNotFound("User not found")
        return user

    def __check_password(self, password: str, hashed_password: str) -> None:
        correct_pw = self.__password_handler.check_password(password, hashed_password)
        if not correct_pw:
            raise HttpBadRequest("Wrong password")
        
    def __create_token(self, user_id:int, username: str) -> str:
        body = {"user_id": user_id, "username": username}
        token = self.__jwt_handler.create_jwt_token(body)
        return token

    def __format_response(self, username: str, token: str) -> dict:
        return {
                "access": True,
                "username": username,
                "authorization": token
            }
