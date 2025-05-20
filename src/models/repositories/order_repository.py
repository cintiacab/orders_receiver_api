from sqlite3 import Connection
from src.models.repositories.interface.order_repository import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def order_registry(self, description: str, user_id: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO orders
                (description, user_id)
            VALUES
                (?, ?)
            """,
            (description, user_id)
        )
        self.__conn.commit()

    def list_orders(self, user_id: int) -> list:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, username, password
            FROM orders
            WHERE user_id = ?
            """, (user_id,)
        )
        orders = cursor.fetchall()
        return orders
