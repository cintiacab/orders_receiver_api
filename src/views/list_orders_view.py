from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.list_orders import ListOrdersInteface
from src.errors.errors_types.http_bad_request_error import HttpBadRequest

class ListOrdersView:
    def __init__(self, controller: ListOrdersInteface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_id = http_request.headers.get("uid")
        self.__validate_input(user_id, header_id)
        response = self.__controller.list_orders(user_id)
        return HttpResponse(body= response, status_code= 200)
    
    def __validate_input(self, user_id: any, header_id: any)  -> None:
        if int(header_id) != int(user_id):
            raise HttpBadRequest("Invalid Input")
