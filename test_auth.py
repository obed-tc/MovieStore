import unittest
from unittest.mock import MagicMock
from auth import hash_password, store_user, authenticate

def test_hash_password():
    # Prueba la función hash_password
    password = "testpassword"
    hashed_password, salt = hash_password(password)

    assert hashed_password is not None
    assert salt is not None

def test_store_user():
    # Prueba la función store_user
    mock_cursor = MagicMock()
    mock_connection = MagicMock()

    username = "testuser"
    password = "testpassword"
    role = "testrole"

    result = store_user(username, password, role, mock_cursor, mock_connection)

    assert result is True
    mock_cursor.execute.assert_called_once()

def test_authenticate():
    # Prueba la función authenticate
    mock_cursor = MagicMock()

    username = "testuser"
    password = "testpassword"
    role = "testrole"

    # Simula la existencia del usuario en la base de datos
    mock_cursor.fetchone.return_value = ("hashed_password", "salt", role)

    result = authenticate(username, password, mock_cursor)

    assert result is not None
    assert result == ("hashed_password", "salt", role)

if __name__ == '__main__':
    unittest.main()
