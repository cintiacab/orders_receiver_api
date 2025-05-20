from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .list_users_view import ListUserView

class MockController:
    def list_all(self) -> dict:
        return {"data": {"answer": "Dict"}}
    
def test_handle():
    controller = MockController()
    repo = ListUserView(controller)
    http_request = HttpRequest()
    response = repo.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {"data": {"answer": "Dict"}}
