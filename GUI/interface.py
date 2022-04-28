import os
import sys
import threading
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation, QObject, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QDesktopWidget, QTableView
from system_gui import Ui_MainWindow
from antivirus_package import InfoSystem, PortScanner, Monitor, UsbLock
from server_package import Server
from database_package import CustomsofficersDataBase
from logging_package import Logging
import time


class ActivityRegistrationThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ActivityRegistrationThread, self).__init__()
        self.monitor_creation = Monitor("creation")
        self.monitor_deletion = Monitor("deletion")

    def run(self):
        self.monitor_creation.main()
        self.monitor_deletion.main()
        time.sleep(5)
        while True:
            time.sleep(3)
            try:
                with open("C:\\PycharmProjects\\Antivirus\\antivirus_package\\activity_registration.txt", "r") as file:
                    res = file.readlines()
                    for i in res:
                        self.signal.emit(str(i))
            except FileExistsError as err:
                self.signal.emit("НЕТ ДАННЫХ!")


class PortScannerThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, value):
        super(PortScannerThread, self).__init__()
        self.port_scanner = PortScanner()
        self.value = value

    def run(self):
        res = self.port_scanner.main(self.value)
        self.signal.emit(res)


class CheckUsbThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(CheckUsbThread, self).__init__()
        self.check_usb = UsbLock()

    def run(self):
        while True:
            self.check_usb.main()
            try:
                with open("C:\\PycharmProjects\\Antivirus\\antivirus_package\\locked_usb.txt", "r", encoding="utf-8") as file:
                    res = file.readlines()
                    for i in res:
                        self.signal.emit(str(i))
            except FileExistsError as err:
                self.signal.emit("НЕТ ДАННЫХ!")


class ServerThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ServerThread, self).__init__()

    def run(self):
        try:
            with open("C:\\PycharmProjects\\Antivirus\\logging_package\\server_action.txt", "r", encoding="utf-8") as file:
                while True:
                    # считываем строку
                    line = file.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        continue
                    # выводим строку
                    self.signal.emit(str(line))
        except FileExistsError as err:
            return


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.info = InfoSystem() # информация о системе
        self.usb_blocking = UsbLock() # блокировка usb
        self.port_scanner = PortScanner() # сканер портов
        self.server = Server()
        self.customs_officers_database = CustomsofficersDataBase()
        self.dependencies_path = "C:\\PycharmProjects\\dependencies\\"
        self.text = self.ui.comboBox_port_scanner.currentText()

        # захват размера окна для изменения размера окна
        # QSizeGrip(self.ui.size_grip)

        # удаляем заголовок
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # делаем главный экран прозрачным
        self.setAttribute(QtCore.Qt.WA_AttributeCount)

        # устанавливаем загаловок
        self.setWindowTitle("СИСТЕМА ОБЕСПЕЧЕНИЯ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ")

        # устновка окна по умолчанию
        self.ui.stackedWidget.setCurrentWidget(self.ui.authorization_page)

        # настрйока кнопки входа
        self.ui.btn_login.clicked.connect(lambda: self.login_into_system())

        # сварачиваем окно
        self.ui.btn_minimize_window.clicked.connect(lambda: self.showMinimized())

        # свернуть/развернуть окно
        self.ui.btn_restore_window.clicked.connect(lambda: self.restore_or_maximize_window())

        # настройки кнопки выхода
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_close_window.clicked.connect(self.close)

        # кнопка главной страницы
        self.ui.btn_main_page_manual.clicked.connect(lambda: self.show_main_manual())

        ######################################
        # настройка кнопок модуля антивируса #
        ######################################
        self.ui.btn_antivirus_manual.clicked.connect(lambda: self.show_antivirus_manual())
        self.ui.btn_information_about_system.clicked.connect(lambda: self.show_information_about_system())

        # настройка регистрации активности
        self.activity_registration_thread = ActivityRegistrationThread()
        self.activity_registration_thread.signal.connect(self.insert_activity_registration_value)
        self.ui.btn_activity_registration.clicked.connect(lambda: self.show_activity_registration_page())
        self.ui.btn_start_activity_registration.clicked.connect(self.start_activity_registration_thread)

        # настройка проверки файла
        self.ui.btn_check_file.clicked.connect(self.show_check_file)
        self.ui.btn_start_file_checking.clicked.connect(self.test_file_check)

        # блокировка usb
        self.usb_blocking_thread = CheckUsbThread()
        self.usb_blocking_thread.signal.connect(self.insert_info_about_blocking_usb)
        self.ui.btn_check_usb.clicked.connect(lambda: self.show_usb_block())
        self.ui.btn_start_usb_blocking.clicked.connect(lambda: self.insert_information_about_usb())

        # настройка порт сканер
        self.port_scanner_thread = PortScannerThread(self.ui.comboBox_port_scanner.currentText())
        self.port_scanner_thread.signal.connect(self.insert_value)
        self.ui.btn_start_port_scanner.clicked.connect(self.start_port_scanner_thread)
        self.ui.btn_port_scaner.clicked.connect(lambda: self.show_port_scanner())

        ######################################
        # настройка кнопок модуля сервер     #
        ######################################
        self.server_thread = ServerThread()
        self.server_thread.signal.connect(self.insert_server_value)
        self.ui.btn_show_info_server.clicked.connect(self.start_show_info)
        self.ui.btn_show_server_page.clicked.connect(lambda: self.show_server_page())
        self.ui.btn_start_server.clicked.connect(self.start_server_thread)

        ######################################
        # настройка кнопок модуля СУБД       #
        ######################################
        # обновление базы данных
        self.refresh_timer = QTimer(self)
        self.refresh_timer.setSingleShot(True)
        self.refresh_timer.setInterval(1000)
        self.refresh_timer.timeout.connect(self.onModificarTimer_timeout)

        # открыть страницу связанную с БД
        self.ui.btn_show_database.clicked.connect(lambda: self.show_dbms_page())
        self.ui.btn_dbms_manual.clicked.connect(lambda: self.show_dbms_manual())

        # добавление новых пользователей
        self.ui.btn_add_new_user.clicked.connect(lambda: self.get_data_from_le())

        # поиск записей в базе данных
        self.searchModel = QSqlQueryModel(self)
        self.searchModel.setQuery("""SELECT * FROM `customs_officers`;""")
        self.ui.search_table_view.setModel(self.searchModel)
        self.ui.le_search_data_in_db.textEdited.connect(self.search_user_in_db)

        # зменение записей в базе данных
        self.changeModel = QSqlTableModel(self)
        self.changeModel.setTable("customs_officers")
        self.changeModel.select()
        self.ui.change_table_view.setModel(self.changeModel)
        self.changeModel.beforeUpdate.connect(self.onmodificarModel_beforeUpdate)

        # удаление записей из БД
        self.deleteModel = QSqlTableModel(self)
        self.deleteModel.setTable("customs_officers")
        self.deleteModel.select()
        self.ui.delete_table_view.setModel(self.deleteModel)
        self.ui.delete_table_view.setEditTriggers(QTableView.NoEditTriggers)
        self.ui.delete_table_view.setSelectionBehavior(QTableView.SelectRows)
        self.ui.delete_table_view.clicked.connect(self.delete_user_from_db)

        ###############################################
        # настройка кнопок модуля журнала лоигрвоания #
        ###############################################
        self.ui.btn_open_action_log.clicked.connect(self.show_logs_and_get_logs)
        self.ui.btn_action_log_manual.clicked.connect(self.show_action_log_manual)

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

    # открыть страницу с информацией о системе
    def show_main_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_system)

    # вход в систему
    def login_into_system(self):
        __login = self.ui.le_login.text()
        __password = self.ui.le_password.text()
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_container_page)
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_system)

    # регистрация в системе
    def registration(self):
        pass

    ########################
    # РАБОТА С АНТИВИРУСОМ #
    ########################
    def show_antivirus_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_antivirus)

    def test_file_check(self):
        res = self.ui.cb_fast_check.text()
        print(res)

    ##########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ С РЕГИСТРАЦИЕЙ АКТИВНОСТИ #
    ##########################################################
    def show_activity_registration_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_registration_activity)

    def insert_activity_registration_value(self, value):
        self.ui.plainTextEdit_for_activity_registration.appendPlainText(value)

    def start_activity_registration_thread(self):
        self.activity_registration_thread.start()

    #########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ С ПРОВЕРКОЙ ФАЙЛА        #
    #########################################################
    def show_check_file(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_check_file)


    #########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ ВЫВОДА ИНФОРМАЦИИ О СИСТЕМЕ     #
    #########################################################
    def show_information_about_system(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_information_about_system)
        system_info = self.info.main()
        self.ui.textEdit__information_about_system.setPlainText(system_info)


    #########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ БЛОКИРОВКИ USB                  #
    #########################################################
    def show_usb_block(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usb_lock)

    def insert_information_about_usb(self):
        existent_disks, non_existent_disks = self.usb_blocking.monitorUSBStorage()
        self.ui.textEdit_usb_blocking.setPlainText(existent_disks)
        self.usb_blocking_thread.start()

    def insert_info_about_blocking_usb(self, value):
        # self.ui.textEdit_usb_blocking.setPlainText(value)
        self.ui.te_list_of_locked_usb.setPlainText(value)

    #############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ ПОРТ СКАНЕРА #
    #############################################
    def start_port_scanner_thread(self):
        self.ui.plainTextEdit_port_scanner.appendPlainText("Запуск сканера портов")
        self.port_scanner_thread.start()

    def show_port_scanner(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_port_scanner)

    def insert_value(self, value):
        self.ui.plainTextEdit_port_scanner.appendPlainText(value)
        self.ui.plainTextEdit_port_scanner.appendPlainText("....")

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ БЛОКИРОВКИ IP #
    ##############################################
    def IP_block(self):
        ...

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ С СЕРВЕРОМ           #
    ##############################################
    def show_server_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_server_info)

    def start_server_thread(self):
        server_thread = threading.Thread(target=self.server.main)
        server_thread.start()

    def start_show_info(self):
        self.server_thread.start()

    def insert_server_value(self, value):
        self.ui.plainTextEdit_infromation_from_server.appendPlainText(value)


    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ С БАЗОЙ ДАННЫХ       #
    ##############################################
    # создание таблицы
    # def prepareDatabase(self):
    #     db_name = self.customs_officers_database.db_name
    #     create_table_query = self.customs_officers_database.create_db()
    #     db = QSqlDatabase().addDatabase("QSQLITE")
    #     # db.setDatabaseName(self.dependencies_path+db_name)
    #     db.setDatabaseName(db_name)
    #     if db.open():
    #         query = QSqlQuery()
    #         if query.prepare(create_table_query):
    #             if query.exec_():
    #                 print("ТАБЛИЦА УСПЕШНО СОЗДАНА!")
    #                 self.refreshTable()

    # получаем данные и вставляем в таблицу
    def get_data_from_le(self):
        name = self.ui.le_name.text()
        soname = self.ui.le_soname.text()
        rank = self.ui.le_rank.text()
        email = self.ui.le_email.text()
        login = self.ui.le_login_2.text()
        password = self.ui.le_password_2.text()
        access_level = self.ui.le_access_level.text()
        # print(name, soname, rank, email, login, password, access_level)

        data = {}
        data["name"] = name
        data["soname"]  = soname
        data["rank"] = rank
        data["email"] = email
        data["login"] = login
        data["password"] = password
        data["access_level"] = access_level

        for key in data:
            if data.get(key) == "":
                QtWidgets.QMessageBox.critical(self, "ERROR", "Поля ввода не должны быть пустыми!")
                return

        access_level = int(access_level)
        query = QSqlQuery()
        insert_query = self.customs_officers_database.insert_data_into_db()
        if query.prepare(insert_query):
            query.addBindValue(name)
            query.addBindValue(soname)
            query.addBindValue(rank)
            query.addBindValue(email)
            query.addBindValue(login)
            query.addBindValue(password)
            query.addBindValue(access_level)
            if query.exec_():
                QtWidgets.QMessageBox.information(self, "Уведомление", "Данные успешно давлены")
                self.ui.le_name.clear()
                self.ui.le_soname.clear()
                self.ui.le_rank.clear()
                self.ui.le_email.clear()
                self.ui.le_login_2.clear()
                self.ui.le_password_2.clear()
                self.ui.le_access_level.clear()
                self.refreshTable() # обновляем базу данных

    # поиск пользователя в БД
    def search_user_in_db(self, data):
        query = self.customs_officers_database.search_user_from_db(data)
        self.searchModel.setQuery(query)

    # удаления пользователя из БД
    def delete_user_from_db(self, idx):
        if QtWidgets.QMessageBox.question(self, "Вопрос", "Вы точно уверены что хотите удалить?",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            row = idx.row()
            if self.deleteModel.removeRow(row):
                self.refreshTable()

    # обновление таблицы
    def refreshTable(self):
        self.searchModel.setQuery("""SELECT * FROM `customs_officers`;""")
        self.changeModel.select()
        self.deleteModel.select()

    def onModificarTimer_timeout(self):
        self.refreshTable()

    def onmodificarModel_beforeUpdate(self, row, record):
        self.refresh_timer.start()

    def show_dbms_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_show_dbms)

    def show_dbms_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_dbms_manual)

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ ЖУРНАЛА ЛОГИРОВАНИЯ  #
    ##############################################
    def show_action_log_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_show_action_log_manual)

    def show_logs_and_get_logs(self):
        self.ui.lw_log_widget.clear()
        path = "C:\\PycharmProjects\\Antivirus\\logging_package"
        dirs = os.listdir(path)
        logs = [file for file in dirs if file.endswith("txt")]
        if len(logs) > 0:
            for log in logs:
                self.ui.lw_log_widget.addItem(log)
        else:
            self.ui.lw_log_widget.addItem("ЖУРНАЛЫ ДЕЙСТВИЙ ОТСУТСТВУЮТ")
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_show_logging_journal)
        self.ui.lw_log_widget.itemClicked.connect(self.onClicked)

    def onClicked(self, item):
        self.ui.pte_log_action.clear()
        file = item.text()
        path = f"C:\\PycharmProjects\\Antivirus\\logging_package\\{file}"
        with open(path, "r", encoding="utf-8") as file:
            res = file.readlines()
            for i in res:
                self.ui.pte_log_action.appendPlainText(i)

def prepareDatabase():
    db = QSqlDatabase().addDatabase("QSQLITE")
    # db.setDatabaseName(self.dependencies_path+db_name)
    db.setDatabaseName("customs_officers.db")
    if db.open():
        query = QSqlQuery()
        if query.prepare("""
        CREATE TABLE IF NOT EXISTS `customs_officers` (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            soname TEXT,
            rank TEXT,
            email TEXT,
            login TEXT,
            password TEXT,
            access_level INTEGER);"""):
            if query.exec_():
                print("ТАБЛИЦА УСПЕШНО СОЗДАНА!")

def main():
    app = QtWidgets.QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    # my_window.prepareDatabase()
    sys.exit(app.exec_())


def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        window, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)

sys.excepthook = my_excepthook

if __name__ == '__main__':
    # точка входа в программу
    # app = QtWidgets.QApplication(sys.argv)
    # my_window = MyWindow()
    # my_window.show()
    # sys.exit(app.exec_())
    prepareDatabase()
    main()

    #
    # class MainWindow(QMainWindow, Ui_MainWindow):
    #     def __init__(self):
    #         super().__init__()
    #
    #         self.setupUi(self)
    #
    #         self.myList = ['Item 1', 'Item 2', 'Item 3', 'Item 4', ]
    #         self.listWidget.addItems(self.myList)
    #
    #         self.listWidget.itemClicked.connect(self.onClicked)
    #
    #     def onClicked(self, item):
    #         print(f'\nitem: {item}')  #
    #         print(f'item.text: {item.text()}')  #