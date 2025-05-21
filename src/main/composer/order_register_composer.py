from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.order_repository import OrderRepository
from src.controllers.order_register import OrderRegister
from src.views.order_register_view import OrderRegisterView

def order_register_composer():
    conn = db_connection_handler.get_connection()
    model = OrderRepository(conn)
    controller = OrderRegister(model)
    view = OrderRegisterView(controller)
    return view
