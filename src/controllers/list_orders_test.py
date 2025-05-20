from .list_orders import ListOrders

class MockRepository:
    def list_orders(self, user_id: int) -> list:
        return [
            (1, "description1", '2025-05-20 14:32:15', 5),
            (2, "description2", '2025-05-19 09:45:00', 5),
            (3, "description3", '2025-05-18 19:23:00', 5)
        ]

def test_list_orders():
    repo = MockRepository()
    controller = ListOrders(repo)
    response = controller.list_orders(5)

    expected_response = {
            "data":{
                "type" : "orders",
                "count": 3,
                "attributes":[
                    { "id": 1, "description": "description1", "created_in": '2025-05-20 14:32:15'},
                    { "id": 2, "description": "description2", "created_in": '2025-05-19 09:45:00'},
                    { "id": 3, "description": "description3", "created_in": '2025-05-18 19:23:00'}
                ]
            }
        }  
    assert response == expected_response
