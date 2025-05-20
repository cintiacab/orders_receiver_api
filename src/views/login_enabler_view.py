from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.login_enabler import LoginEnablerInterface

class LoginEnablerView:
    def __init__(self, controller: LoginEnablerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")
        self.__validate_inputs(username, password)
        response = self.__controller.login(username, password)
        return HttpResponse(body=response, status_code= 200)
    
    def __validate_inputs(self, username: any, password: any) -> None:
        if(
            not username or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ): raise Exception("Invalid Input")
