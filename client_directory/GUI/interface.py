import json
import os
import sys
import socket
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, QThread
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit
# from ..test_client import Client
from client_directory.test_client import Client
# from client_directory.client import Client
import icons_rc_2
from client_gui import Ui_MainWindow
from logging_package.main import Logging


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
        self.logger = Logging()

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

        # отображаем новые базы данных
        self.ui.btn_open_list_of_db.clicked.connect(lambda: self.open_page_list_of_db())

        # настройка ввода пароля
        self.ui.le_password.setEchoMode(QLineEdit.Password)
        self.ui.le_email_code.setEchoMode(QLineEdit.Password)

        # настройка кнопок с клавиатуры
        self.ui.btn_login.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_password.returnPressed.connect(self.ui.btn_login.click)  # нажатие <Enter>

        self.ui.btn_accept_code.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_email_code.returnPressed.connect(self.ui.btn_accept_code.click)  # нажатие <Enter>

    # вход в систему
    def login(self):
        path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"
        login = self.ui.le_login.text()
        password = self.ui.le_password.text()
        try:
            client.connect_to_server(SERVER_ADDRESS)
            client.send_user_data(login, password)
        except socket.error as err:
            print(89)
        time.sleep(10)
        with open(path, "r") as file:
            res = file.readline()
            if res.strip() == "True":
                self.ui.stackedWidget.setCurrentWidget(self.ui.two_factor_authentication_page)
                self.logger.register_user_actions(f"Вход в программу пользвоателя: {login}")
            else:
                QtWidgets.QMessageBox.information(self, "Ошбика", "Неверный адрес электронной почты или пароль")
                self.logger.register_user_actions(f"Неудачный вход в программу пользвоателя: {login}")


    def show_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_container_page)
        self.logger.register_user_actions(f"Открыл главную страницу")

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

    # страница с доступынми базами данных
    def open_page_list_of_db(self):
        self.ui.lw_db_widget.clear()
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\database_dir"
        dirs = os.listdir(path)
        dbs = [file for file in dirs]
        if len(dbs) > 0:
            for db in dbs:
                self.ui.lw_db_widget.addItem(db)
        else:
            self.ui.lw_db_widget.addItem("БАЗЫ ДАННЫХ ОТСУТСТВУЮТ")
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_list_of_db)
        self.ui.lw_db_widget.itemClicked.connect(self.onDBClicked)
        self.ui.tv_for_db_view.setDisabled(True) # не даёт взаимодействовать с таблицей
        self.logger.register_user_actions("Открыл страницу с базами данных")

    # открывает базу данных
    def onDBClicked(self, item):
        self.ui.lw_table_widget.clear()
        file = item.text()
        path = f"C:\\PycharmProjects\\Antivirus\\dependencies\\database_dir\\{file}"

        # открываем базу данных по путю
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(path)
        self.db.open()

        # поиск таблиц в базе данных
        model = QSqlQueryModel()
        model.setQuery(
            """SELECT name FROM sqlite_master WHERE type='table';""")  # делаем запрос с логином из поля ввода
        for i in range(5):  # при помощи получаем его данные
            res = model.record(i).value("name")
            self.ui.lw_table_widget.addItem(res)
        self.ui.lw_table_widget.itemClicked.connect(self.onTableClicked)
        self.logger.register_user_actions(f"открыл базу данных: {item}")

    # отображаем таблицу
    def onTableClicked(self, item):
        table = item.text()

        # отображаем базу данных в таблице
        self.model = QSqlTableModel(self)
        self.model.setTable(table)
        self.model.select()

        # растягиваем таблицу по всей ширине
        header = self.ui.tv_for_db_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tv_for_db_view.setModel(self.model)
        self.logger.register_user_actions(f"отобразил базу данных: {item}")

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