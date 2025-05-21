from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.order_register import OrderRegisterInterface

class OrderRegisterView:
    def __init__(self, controller: OrderRegisterInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        description = http_request.body.get("description")
        user_id = http_request.params.get("user_id")
        header_id = http_request.headers.get("uid")
        self.__validate_input(user_id, description, header_id)
        response = self.__controller.registry(user_id, description)
        return HttpResponse(body=response, status_code=201)

    def __validate_input(self, user_id: any, description: any, header_id: any)  -> None:
        if (not user_id or not description
            or not isinstance (description, str)
            or int(header_id) != int(user_id)
        ): 
            raise Exception("Invalid Input")
