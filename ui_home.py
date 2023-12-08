from PyQt5 import QtCore, QtGui, QtWidgets
from eventbus import EventBus
from notification import user_notification_handler
from PyQt5.QtCore import Qt, QPropertyAnimation
from conexion import create_connection
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
import webbrowser

from addmoviedialog import AddMovieDialog
class Ui_MainWindow(object):
    def __init__(self):
        self.event_bus = EventBus()
    def subscribe_to_movie_notifications(self, user_data):

        self.button_suscribir.hide()
        self.button_suscrito.show()
        user_name = user_data.get("username", "Usuario")
        self.event_bus.subscribe("nueva_pelicula", lambda data: user_notification_handler(data, user_data,self.label_3,self.widget_notification,self.notification_timer))

    def unsubscribe_from_movie_notifications(self, user_data):
        self.button_suscribir.show()
        self.button_suscrito.hide()
        user_name = user_data.get("username", "Usuario")
        self.event_bus.unsubscribe("nueva_pelicula", lambda data: user_notification_handler(data, user_name))
    def mostrar_formulario(self):
        dialog = AddMovieDialog()
        dialog.event_bus = self.event_bus
        dialog.exec_()
    def hide_notification(self):
        self.widget_notification.hide()
        self.notification_timer.stop()
    def update_movie_list(self):
        try:
            connection = create_connection()

            if not connection:
                print("Error de conexión a la base de datos.")
                return

            for i in reversed(range(self.verticalLayout_6.count())):
                widgetToRemove = self.verticalLayout_6.itemAt(i).widget()
                if widgetToRemove is not None:
                    widgetToRemove.setParent(None)

            with connection.cursor() as cursor:
                select_movies_query = "SELECT id, nombre, descripcion FROM peliculas"
                cursor.execute(select_movies_query)
                result = cursor.fetchall()

                for movie in result:
                    self.add_movie_widget(movie)

        except Exception as e:
            print(f"Error al obtener películas de la base de datos: {e}")

        finally:
            connection.close()

    def add_movie_widget(self, movie):
        widget = QWidget()
        widget.setMinimumSize(0, 100)

        layout = QHBoxLayout(widget)

        if isinstance(movie, tuple) and len(movie) >= 3:
            id_pelicula, nombre, descripcion = movie[:3]  
        else:
            print(f"Error: La tupla de película no tiene la estructura esperada: {movie}")
            return

        button = QPushButton(nombre)
        button.setFont(QtGui.QFont("", 12, QtGui.QFont.Bold))
        button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        button.setStyleSheet("border:None")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/a/imgs/iconopelicula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon5)
        button.setIconSize(QtCore.QSize(50, 50))
        button.clicked.connect(lambda: self.show_movie_details(movie))
        layout.addWidget(button)

        label_descripcion = QLabel(descripcion)
        layout.addWidget(label_descripcion)
        checkWidget = QtWidgets.QWidget(widget)
        checkWidget.setMaximumSize(QtCore.QSize(40, 40))
        checkWidget.setStyleSheet("\n"
                                            "border-image:url(:/a/imgs/check.png)\n"
                                            "\n"
                                            "")
        checkWidget.setObjectName("widgetCheck")
        self.verticalLayout_6.insertWidget(self.verticalLayout_6.count() - 1, widget)

    def show_movie_details(self, movie):
        print(f"Mostrar detalles de la película: {movie}")
        webbrowser.open(movie[-1])

    def open_login_window(self):
        print(self.login_window)
        self.login_window.show()
        self.homeWindow.close()
    def setupUi(self, MainWindow, user_data=None,loginWindows=None):
        self.login_window=loginWindows
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 600)
        MainWindow.showMaximized()
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("background-color:rgb(24, 24, 24);\n"
                                 "color:white")
        self.homeWindow=MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalWidget.setStyleSheet("padding:20px")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalWidget_4 = QtWidgets.QWidget(self.horizontalWidget)
        self.verticalWidget_4.setMinimumSize(QtCore.QSize(100, 100))
        self.verticalWidget_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.verticalWidget_4.setStyleSheet("\n"
                                           "border-image:url(:/a/imgs/logo.png)\n"
                                           "\n"
                                           "")
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3.addWidget(self.verticalWidget_4)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_4.setStyleSheet("color:#c83218;\n"
                                   "font: 87 22pt \"Arial Black\";\n"
                                   "margin:0px;\n"
                                   "padding:0")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.button_publicar = QtWidgets.QPushButton(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_publicar.setFont(font)
        self.button_publicar.setStyleSheet("border:None")
        self.button_publicar.clicked.connect(self.mostrar_formulario)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/a/imgs/addicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_publicar.setIcon(icon)
        self.button_publicar.setIconSize(QtCore.QSize(40, 40))
        self.button_publicar.setObjectName("button_publicar")
        self.horizontalLayout_3.addWidget(self.button_publicar)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white;\n"
                                      "border:None")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/a/imgs/usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.button_salir = QtWidgets.QPushButton(self.horizontalWidget)
        self.button_salir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_salir.setStyleSheet("border:None")
        self.button_salir.setText("")
        self.button_salir.clicked.connect(self.open_login_window)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/a/imgs/salir.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_salir.setIcon(icon2)
        self.button_salir.setIconSize(QtCore.QSize(25, 25))
        self.button_salir.setObjectName("button_salir")
        self.horizontalLayout_3.addWidget(self.button_salir)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.widget_notification = QtWidgets.QWidget(self.centralwidget)
        self.widget_notification.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_notification.setStyleSheet("background-color:rgb(23, 199, 4)")
        self.widget_notification.setObjectName("widget_notification")
        self.widget_notification.hide()
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_notification)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_notification)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.widget_notification)
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.verticalWidget_2)
        self.label.setStyleSheet("background-color:None;\n"
                                "font: 87 22pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.button_reload = QtWidgets.QPushButton(self.verticalWidget_2)
        self.button_reload.setMaximumSize(QtCore.QSize(50, 50))
        self.button_reload.setStyleSheet("border:None")
        self.button_reload.setText("")
        self.button_reload.clicked.connect(self.update_movie_list)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/a/imgs/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_reload.setIcon(icon3)
        self.button_reload.setIconSize(QtCore.QSize(30, 30))
        self.button_reload.setObjectName("button_reload")
        self.horizontalLayout_7.addWidget(self.button_reload)
        self.button_suscrito = QtWidgets.QPushButton(self.verticalWidget_2)
        self.button_suscrito.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_suscrito.setFont(font)
        self.button_suscrito.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_suscrito.setStyleSheet("border:None;\n"
                                           "color:red")
        icon4 = QtGui.QIcon()
        self.button_suscrito.hide()
        icon4.addPixmap(QtGui.QPixmap(":/a/imgs/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_suscrito.setIcon(icon4)
        self.button_suscrito.setIconSize(QtCore.QSize(25, 25))
        self.button_suscrito.setObjectName("button_suscrito")
        self.button_suscrito.clicked.connect(lambda: self.unsubscribe_from_movie_notifications(user_data))
        self.horizontalLayout_7.addWidget(self.button_suscrito)
        self.button_suscribir = QtWidgets.QPushButton(self.verticalWidget_2)
        self.button_suscribir.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_suscribir.setFont(font)
        self.button_suscribir.clicked.connect(lambda: self.subscribe_to_movie_notifications(user_data))
        self.button_suscribir.setStyleSheet("background-color:red")
        self.button_suscribir.setObjectName("button_suscribir")
        self.horizontalLayout_7.addWidget(self.button_suscribir)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.widget_pelicula = QtWidgets.QWidget(self.verticalWidget_2)
        self.widget_pelicula.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_pelicula.setObjectName("widget_pelicula")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_pelicula)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_pelicula)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("border:None")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/a/imgs/iconopelicula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.label_descripcion = QtWidgets.QLabel(self.widget_pelicula)
        self.label_descripcion.setObjectName("label_descripcion")
        self.horizontalLayout_5.addWidget(self.label_descripcion)
        self.verticalWidget_21 = QtWidgets.QWidget(self.widget_pelicula)
        self.verticalWidget_21.setMaximumSize(QtCore.QSize(40, 40))
        self.verticalWidget_21.setStyleSheet("\n"
                                            "border-image:url(:/a/imgs/check.png)\n"
                                            "\n"
                                            "")
        self.verticalWidget_21.setObjectName("verticalWidget_21")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5.addWidget(self.verticalWidget_21)
        self.verticalLayout_6.addWidget(self.widget_pelicula)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.verticalWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.notification_timer = QtCore.QTimer()
        self.notification_timer.timeout.connect(self.hide_notification)
        self.update_movie_list()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, user_data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, user_data):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "PeliUAB"))
        self.button_publicar.setText(_translate("MainWindow", "Publicar película"))
        print(user_data.get("role"))
        if ( user_data.get("role")=="cliente"):
            self.button_publicar.hide()
        self.pushButton.setText(_translate("MainWindow", user_data.get("username", "Usuario")))
        self.label_3.setText(_translate("MainWindow", "Se acaba de publicar una nueva película"))
        self.label.setText(_translate("MainWindow", "Películas"))
        self.button_suscrito.setText(_translate("MainWindow", "Suscrito"))
        self.button_suscribir.setText(_translate("MainWindow", "Suscribirme"))
        self.pushButton_2.setText(_translate("MainWindow", "Nombre de la película"))
        self.label_descripcion.setText(_translate("MainWindow", "Esta es toda la descripción"))
