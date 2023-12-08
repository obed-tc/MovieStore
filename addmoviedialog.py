from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from conexion import create_connection

class AddMovieDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agregar Nueva Película")

        layout = QVBoxLayout()

        self.label_nombre = QLabel("Nombre:")
        self.edit_nombre = QLineEdit()

        self.label_descripcion = QLabel("Descripción:")
        self.edit_descripcion = QLineEdit()

        self.button_agregar = QPushButton("Agregar")
        self.button_agregar.clicked.connect(self.agregar_pelicula)

        layout.addWidget(self.label_nombre)
        layout.addWidget(self.edit_nombre)
        layout.addWidget(self.label_descripcion)
        layout.addWidget(self.edit_descripcion)
        layout.addWidget(self.button_agregar)

        self.setLayout(layout)

    def agregar_pelicula(self):
        nombre = self.edit_nombre.text()
        descripcion = self.edit_descripcion.text()

        # Establecer conexión a la base de datos
        connection = create_connection()

        if not connection:
            print("Error de conexión a la base de datos.")
            return

        try:
            with connection.cursor() as cursor:
                insert_movie_query = "INSERT INTO peliculas (nombre, descripcion) VALUES (%s, %s)"
                cursor.execute(insert_movie_query, (nombre, descripcion))
                connection.commit()
                print("Película agregada a la base de datos.")

                # Publicar el evento utilizando el EventBus
                data = {"nombre": nombre, "descripcion": descripcion}
                self.event_bus.publish("nueva_pelicula", data)

        except Exception as e:
            print(f"Error al agregar la película a la base de datos: {e}")

        finally:
            connection.close()

        # Cerrar el formulario
        self.accept()
