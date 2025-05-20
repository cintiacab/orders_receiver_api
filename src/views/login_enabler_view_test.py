from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .login_enabler_view import LoginEnablerView

class MockController:
    def login(self, username: str, password: str) -> dict:
        return {"data": {"answer": "Dict"}}

def test_handle():
    body ={
        "username": "user1",
        "password": "my_pwd"
    }
    controller = MockController()
    repo = LoginEnablerView(controller)
    http_request = HttpRequest(body=body)
    response = repo.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {"data": {"answer": "Dict"}}
