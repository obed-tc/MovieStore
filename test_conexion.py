import unittest
from unittest.mock import patch
from conexion import create_connection

class TestCreateConnection(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_create_connection_success(self, mock_connect):
        mock_connection = mock_connect.return_value
        mock_connection.is_connected.return_value = True

        result = create_connection()
        self.assertIsNotNone(result)
        mock_connect.assert_called_once_with(
            host='localhost',
            database='dbmovies',
            user='root',
            password=''
        )



if __name__ == '__main__':
    unittest.main()
