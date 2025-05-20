from src.controllers.interfaces.list_users import ListUserInteface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ListUserView:
    def __init__(self, controller: ListUserInteface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response  = self.__controller.list_all()
        return HttpResponse(body= response, status_code= 200)
