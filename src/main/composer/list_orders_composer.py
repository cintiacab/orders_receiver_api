from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.order_repository import OrderRepository
from src.controllers.list_orders import ListOrders
from src.views.list_orders_view import ListOrdersView

def list_orders_composer():
    conn = db_connection_handler.get_connection()
    model = OrderRepository(conn)
    controller = ListOrders(model)
    view = ListOrdersView(controller)
    return view
