
from getpass import getpass
import bcrypt
from mysql.connector import Error

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password, salt

def store_user(username, password, role, cursor, connection):
    try:
        hashed_password, salt = hash_password(password)

        query = "INSERT INTO users (username, password, salt, role) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (username, hashed_password.decode('utf-8'), bytes(salt), role))
        connection.commit()
        print('Usuario registrado exitosamente')
        return True
    except Error as e:
        print('Error al almacenar usuario:', e)
        return False


def authenticate(username, password, cursor):
    try:
        query = "SELECT password, salt,role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result:
            stored_password, salt,role = result
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bytes(salt))

            if hashed_password == stored_password.encode('utf-8'):
                return result
        return None
    except Error as e:
        print('Error al autenticar:', e)
        return None
