from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .order_register_view import OrderRegisterView

class MockController:
    def registry(self, user_id: int, description: str) -> dict:
        return {"data": {"answer": "Dict"}}
    
def test_handle():
    body ={ "description": "description1" }
    header = {"user_id": 1}
    controller = MockController()
    view = OrderRegisterView(controller)
    http_request = HttpRequest(body=body, headers=header)
    response = view.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == {"data": {"answer": "Dict"}}
