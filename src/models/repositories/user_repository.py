from sqlite3 import Connection
from src.models.repositories.interface.user_repository import UserRepositoryInterface

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
    
    def get_user_by_username(self, username:str) -> tuple[int, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, username, password
            FROM users
            WHERE username = ?
            """, (username,)
        )
        user = cursor.fetchone()
        return user
    
    def get_user_by_id(self, id: int) -> tuple[int, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, username, password
            FROM users
            WHERE id = ?
            """, (id,)
        )
        user = cursor.fetchone()
        return user
   