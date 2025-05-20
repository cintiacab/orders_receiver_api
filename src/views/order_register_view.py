from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.order_register import OrderRegisterInterface

class OrderRegisterView:
    def __init__(self, controller: OrderRegisterInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.headers.get("user_id")
        description = http_request.body.get("description")
        self.__validate_input(user_id, description)
        response = self.__controller.registry(user_id, description)
        return HttpResponse(body=response, status_code=201)

    def __validate_input(self, user_id: any, description: any)  -> None:
        if (not user_id or not description
            or not isinstance (user_id, int)
            or not isinstance (description, str)
        ): 
            raise Exception("Invalid Input")
