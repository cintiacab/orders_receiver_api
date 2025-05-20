from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .list_orders_view import ListOrdersView

class MockController:
    def list_orders(self, user_id: int) -> dict:
        return {"data": {"answer": "Dict"}}

def test_handle():
    header = {"user_id": 1}
    controller = MockController()
    repo = ListOrdersView(controller)
    http_request = HttpRequest(headers=header)
    response = repo.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {"data": {"answer": "Dict"}}
