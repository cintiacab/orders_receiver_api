from .user_repository import UserRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchall = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value = MockCursor())
        self.commit = Mock()

def test_registry_user():
    username = "user1"
    password = "Yabadabadoo"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.user_registry(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password)

def test_list_users():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.list_users()
    
    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    cursor.fetchall.assert_called_once()

def test_get_user_by_username():
    username = "user1"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == ("user1",)
    cursor.fetchone.assert_called_once()