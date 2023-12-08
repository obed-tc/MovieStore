import mysql.connector
from mysql.connector import Error
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dbmovies',
            user='root',
            password=''
        )
        if connection.is_connected():
            print('Conexión exitosa a la base de datos')
            return connection
    except Error as e:
        print('Error al conectar con la base de datos:', e)
        return None