from .order_repository import OrderRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchall = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value = MockCursor())
        self.commit = Mock()

def test_registry_order():
    description  = "Cheese burguer"
    user_id = 1

    mock_connection = MockConnection()
    repo = OrderRepository(mock_connection)
    repo.order_registry(description, user_id)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO orders" in cursor.execute.call_args[0][0]
    assert "(description, user_id)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (description, user_id)

def test_list_orders():
    user_id = 2
    mock_connection = MockConnection()
    repo = OrderRepository(mock_connection)
    repo.list_orders(user_id)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM orders" in cursor.execute.call_args[0][0]
    assert "WHERE user_id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (2,)
    cursor.fetchall.assert_called_once()
