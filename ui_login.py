

from PyQt5 import QtCore, QtGui, QtWidgets
from getpass import getpass
from conexion import create_connection
from auth import  authenticate, store_user
from ui_home import Ui_MainWindow as Ui_HomeWindow
class Ui_MainWindow(object):
    def handle_login(self):
        self.label_2.show()
        if not self.connection or not self.cursor:
            print("Error: No database.")
            return
        username_input = self.lineEdit_2.text()
        password_input = self.lineEdit.text()
        authenticated = authenticate(username_input, password_input, self.cursor)
        if authenticated!=None:
            self.label_2.setStyleSheet("color:green;\n"
"background-color:None;\n"
"font: 11pt \"Arial\";")
            self.label_2.setText("Inicio de sesión exitoso")
            user_data = {"username": username_input, "role": authenticated[-1]}

            self.open_home_window(user_data)
        else:
            self.label_2.setStyleSheet("color:red;\n"
"background-color:None;\n"
"font: 11pt \"Arial\";")
            self.label_2.setText("Usuario o contraseña incorrecto")
    def handle_register(self):
        self.label_2.show()

        if not self.connection or not self.cursor:
            print("Error: No database connection available.")
            return

        username_input = self.lineEdit_2.text()
        password_input = self.lineEdit.text()

        registered = store_user(username_input, password_input, 'cliente', self.cursor, self.connection)

        if registered:
            self.label_2.setStyleSheet("color:green;\n"
"background-color:None;\n"
"font: 11pt \"Arial\";")
            self.label_2.setText("Cuenta creada exitosamente")
        else:
            self.label_2.setStyleSheet("color:red;\n"
"background-color:None;\n"
"font: 11pt \"Arial\";")
            self.label_2.setText("Error al crear la cuenta")
    def open_home_window(self, user_data):
        from ui_home import Ui_MainWindow as Ui_HomeWindow

        self.home_window = QtWidgets.QMainWindow()
        self.ui_home = Ui_HomeWindow()
        self.ui_home.setupUi(self.home_window, user_data,self.loginWindow)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_2.hide()
        self.home_window.show()
        self.loginWindow.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"border-image:url(:/a/imgs/Fondo.jpg);\n"
"padding: 10px;\n"
"}\n"
"")
        self.loginWindow=MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 365))
        self.verticalWidget.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);\n"
"color:white;\n"
"border-radius:10px;\n"
"padding:13px;")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setMaximumSize(QtCore.QSize(1000, 150))
        self.label.setStyleSheet("background-color:None;\n"
"font: 87 22pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalWidget)
        self.lineEdit_2.setStyleSheet("background-color:rgb(212, 212, 212);\n"
"color:black;\n"
"font-size:16px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setStyleSheet("background-color:rgb(212, 212, 212);\n"
"color:black;\n"
"font-size:16px")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setStyleSheet("color:red;\n"
"background-color:None;\n"
"font: 11pt \"Arial\";")
        self.label_2.hide()
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.verticalWidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color:Red;\n"
"font: 12pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handle_login)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalWidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color:None;\n"
"font: 10pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.handle_register)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.verticalWidget)
        spacerItem3 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.connection = create_connection()
        if not self.connection:
            return

        self.cursor = self.connection.cursor()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INICIA SESION"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.label_2.setText(_translate("MainWindow", "Usuario o contraseña incorrecto"))
        self.pushButton.setText(_translate("MainWindow", "Ingresar"))
        self.pushButton_2.setText(_translate("MainWindow", "Registrate"))
import recursos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
