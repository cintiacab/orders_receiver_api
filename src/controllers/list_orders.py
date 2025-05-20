from src.models.repositories.interface.order_repository import OrderRepositoryInterface

class ListOrders:
    def __init__(self, order_repository: OrderRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def list_orders(self, user_id: int) -> dict:
        orders = self.__get_orders(user_id)
        return self.__format_response(orders)

    def __get_orders(self, user_id: int) -> list:
        orders = self.__order_repository.list_orders(user_id)
        return orders
    
    def __format_response(self, orders: list) -> dict:
        formatted_response = []
        for order in orders:
            formatted_response.append({
                "id": order[0],
                "description": order[1],
                "created_in": order[2]
            })

        return {
            "data":{
                "type" : "orders",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
