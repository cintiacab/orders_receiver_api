from .user_register import UserRegister

class MockRepository:
    def __init__(self) -> None:
        self.user_registry_attributes = {}

    def user_registry(self, username: str, password: str) -> None:
        self.user_registry_attributes["username"] = username
        self.user_registry_attributes["password"] = password

def test_registry():
    username = "user2"
    password = "minha_senha"

    repo = MockRepository()
    register_controller = UserRegister(repo)
    response = register_controller.registry(username, password)

    assert response["username"] == username
    assert repo.user_registry_attributes["password"] is not None
    assert repo.user_registry_attributes["password"] != password
