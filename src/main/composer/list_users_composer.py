from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.list_users import ListUser
from src.views.list_users_view import ListUserView

def list_users_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = ListUser(model)
    view = ListUserView(controller)
    return view
