from sqlite3 import Connection
from src.models.interface.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def user_registry(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO users
                (username, password)
            VALUES
                (?, ?)
            """,
            (username, password)
        )
        self.__conn.commit()

    def list_users(self) -> list:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, username, password
            FROM users
            """
        )
        users = cursor.fetchall()
        return users
