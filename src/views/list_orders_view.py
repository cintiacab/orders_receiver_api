from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.list_orders import ListOrdersInteface

class ListOrdersView:
    def __init__(self, controller: ListOrdersInteface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.headers.get("user_id")
        response = self.__controller.list_orders(user_id)
        return HttpResponse(body= response, status_code= 200)
