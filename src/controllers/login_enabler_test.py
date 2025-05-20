from pytest import raises
from .login_enabler import LoginEnabler
from src.drivers.password_handler import PasswordHandler

username = "user1"
password ="my_password"
hashed_password = PasswordHandler().encrypt_password(password)

class MockRepository:
    def get_user_by_username(self, username:str) -> tuple[int, str, str]:
        return (5, username, hashed_password)

def test_login():
    repo = MockRepository()
    login_controller = LoginEnabler(repo)
    response = login_controller.login(username, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["authorization"] is not None

def test_login_with_error():
    repo = MockRepository()
    login_controller = LoginEnabler(repo)
    with raises(Exception):
        login_controller.login(username, "another_password")
