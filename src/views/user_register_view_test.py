from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView

class MockController:
    def registry(self, username: str, password: str) -> dict:
        return {"data": {"answer": "Dict"}}
    
def test_handle():
    body ={
        "username": "user1",
        "password": "my_pwd"
    }
    controller = MockController()
    view = UserRegisterView(controller)
    http_request = HttpRequest(body=body)
    response = view.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == {"data": {"answer": "Dict"}}
