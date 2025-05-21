from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_enabler import LoginEnabler
from src.views.login_enabler_view import LoginEnablerView

def login_enabler_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = LoginEnabler(model)
    view = LoginEnablerView(controller)
    return view
