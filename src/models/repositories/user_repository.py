from sqlite3 import Connection

class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> dict:
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
