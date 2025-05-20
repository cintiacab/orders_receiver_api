from .list_users import ListUser

class MockRepository:
    def list_users(self) -> list:
        return [
            (1, "user1", "password1"),
            (2, "user2", "password2")
        ]

def test_list_all():
    repo = MockRepository()
    user_controller = ListUser(repo)
    response = user_controller.list_all()

    expected_response = {
            "data":{
                "type" : "users",
                "count": 2,
                "attributes": [
                    {"id": 1, "username": "user1"},
                    {"id": 2, "username": "user2"}
                ]
            }
        }

    assert response == expected_response
