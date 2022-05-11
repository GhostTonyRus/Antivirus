import json
import sys
import socket
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, QThread
from PyQt5.QtWidgets import QDesktopWidget
# from ..test_client import Client
from client_directory.test_client import Client
# from client_directory.client import Client
import icons_rc
from client_gui_for_test_2 import Ui_MainWindow


IP = "127.0.0.1"
PORT = 12345
SERVER_ADDRESS = (IP, PORT)


client = Client()

class MyThread(QThread):
    my_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()

    # запуск потока
    def run(self):
        time.sleep(10)
        while True:
            incoming_msg = client.receive_msg()
            if incoming_msg:
                self.my_signal.emit(incoming_msg)
            elif incoming_msg == None or incoming_msg == "":
                break

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.client = Client()

        # удаляем заголовок
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # делаем главный экран прозрачным
        self.setAttribute(QtCore.Qt.WA_AttributeCount)

        # устанавливаем загаловок
        self.setWindowTitle("СИСТЕМА ОБЕСПЕЧЕНИЯ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ")

        # устновка окна по умолчанию
        self.ui.stackedWidget.setCurrentWidget(self.ui.authorization_page)

        # сварачиваем окно
        self.ui.btn_minimize_window.clicked.connect(lambda: self.showMinimized())

        # свернуть/развернуть окно
        self.ui.btn_restore_window.clicked.connect(lambda: self.restore_or_maximize_window())

        # настройки кнопки выхода
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_close_window.clicked.connect(self.close)

        self.ui.btn_login.clicked.connect(lambda: self.login())
        self.ui.btn_accept_code.clicked.connect(lambda: self.show_main_page())

        # настройка кнопок авторизации
        self.ui.btn_open_authorization_page.clicked.connect(lambda: self.show_login_page())
        self.ui.btn_open_authorization_page_2.clicked.connect(lambda: self.show_login_page())

        # запуск сингала для принятия сообщений
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(client.receive_msg)
        self.my_thread.start()

    # вход в систему
    def login(self):
        path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"
        login = self.ui.le_login.text()
        password = self.ui.le_password.text()
        try:
            client.connect_to_server(SERVER_ADDRESS)
            client.send_user_data(login, password)
        except socket.error as err:
            ...
        time.sleep(10)
        with open(path, "r") as file:
            res = file.readline()
            if res == "True":
                print(True)
                self.ui.stackedWidget.setCurrentWidget(self.ui.two_factor_authentication_page)
            else:
                QtWidgets.QMessageBox.information(self, "Ошбика", "Неверный адрес электронной почты или пароль")


    def show_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_container_page)

    # перетаскивание окна
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # изменение размера окна
    def restore_or_maximize_window(self):
        # если окно на максимум
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_app(self):
        sys.exit(0)

    def show_login_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.authorization_page)

if __name__ == '__main__':
    def my_excepthook(type, value, tback):
        QtWidgets.QMessageBox.critical(application, "Critical Error", str(value),
                                       QtWidgets.QMessageBox.Cancel)
        sys.__excepthook__(type, value, tback)

    sys.excepthook = my_excepthook
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())