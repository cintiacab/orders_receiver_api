from .order_register import OrderRegister

class MockOrderRepository:
    def order_registry(self, description: str, user_id: int) -> None: pass

class MockUserRepository:
    def get_user_by_id(self, id: int) -> tuple[int, str, str]:
        return (5, "user1", "my_hash_password")

def test_registry():
    order_repo = MockOrderRepository()
    user_repo = MockUserRepository()
    controller = OrderRegister(order_repo, user_repo)
    description = "Test order"
    response = controller.registry(5, description)

    expected_response = {
            "data": {
                "type": "order",
                "count": 1,
                "description": "Test order"
            }
        }

    assert response == expected_response
