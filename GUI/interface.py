import os
import subprocess
from multiprocessing.pool import ThreadPool
import sys
import threading
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation, QObject, QTimer
from PyQt5.QtGui import QColor, QCloseEvent
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel, QSqlRecord
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QDesktopWidget, QTableView, QLineEdit, \
    QTableWidgetItem
# from system_gui_for_test_2 import Ui_MainWindow
from system_gui_for_test_2_copy import Ui_MainWindow
from database_dialog_view import Ui_Dialog
# from system_gui import Ui_MainWindow
from antivirus_package import Two_factor_authentication, InfoSystem, PortScanner, GetProgramActivity, GetNetworkConnections, GetNetworkStatistics, UsbLock, CheckFile, AntivirusEngine, SystemWatch
from server_package import Server
from database_package import CustomsofficersDataBase
from logging_package import Logging
import time


class ActivityRegistrationThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(ActivityRegistrationThread, self).__init__()
        self.monitor = GetProgramActivity()

    def run(self):
        self.monitor.main()
        time.sleep(10)
        while True:
            time.sleep(3)
            try:
                with open("C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\program_activity.txt", "r",
                          encoding="utf-8") as file:
                    res = file.readlines()
                    for i in res:
                        self.signal.emit(str(i))
            except FileExistsError as err:
                self.signal.emit("НЕТ ДАННЫХ!")

class CheckFilesThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(CheckFilesThread, self).__init__()
        self.check_file = CheckFile()

    def run(self):
        res = self.check_file.main()
        self.signal.emit(res)

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
                with open("C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\locked_usb.txt", "r",
                          encoding="utf-8") as file:
                    res = file.readlines()
                    for i in res:
                        self.signal.emit(str(i))
            except FileExistsError as err:
                self.signal.emit("НЕТ ДАННЫХ!")


class CheckFileThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(CheckFileThread, self).__init__()
        self.check_file = CheckFile()

    def run(self):
        res = self.check_file.main()
        print(res)
        self.signal.emit(res)
        # time.sleep(60)
        # try:
        #     with open("C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\report.txt", "r",
        #               encoding="utf-8") as file:
        #         res = file.readlines()
        #         for i in res:
        #             self.signal.emit(str(i))
        # except FileExistsError as err:
        #     self.signal.emit("НЕТ ДАННЫХ!")

class ServerThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ServerThread, self).__init__()

    def run(self):
        time.sleep(5)
        try:
            with open("C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\temporary_actions.txt", "r",
                      encoding="utf-8") as file:
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


class ThreadProgressBar(QtCore.QThread):
    """
    Runs a counter thread.
    """
    countChanged = QtCore.pyqtSignal(int)

    def run(self):
        for i in range(1, 101):
            time.sleep(60)
            self.countChanged.emit(i)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.check_file = CheckFile()
        self.antivirus_engine = AntivirusEngine()
        self.two_factor_authentication = Two_factor_authentication()
        self.info = InfoSystem()  # информация о системе
        self.usb_blocking = UsbLock()  # блокировка usb
        self.port_scanner = PortScanner()  # сканер портов
        self.system_watch = SystemWatch()
        self.server = Server()
        self.customs_officers_database = CustomsofficersDataBase()
        self.register_actions = Logging()
        self.dependencies_path = "C:\\PycharmProjects\\dependencies\\"
        self.text = self.ui.comboBox_port_scanner.currentText()

        # удаляем заголовок
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # делаем главный экран прозрачным
        self.setAttribute(QtCore.Qt.WA_AttributeCount)

        # устанавливаем загаловок
        self.setWindowTitle("СИСТЕМА ОБЕСПЕЧЕНИЯ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ")

        # устновка окна по умолчанию
        self.ui.stackedWidget.setCurrentWidget(self.ui.authorization_page)

        # настройка кнопок с клавиатуры
        self.ui.btn_login.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_password.returnPressed.connect(self.ui.btn_login.click)  # нажатие <Enter>

        self.ui.btn_accept_code.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_email_code.returnPressed.connect(self.ui.btn_accept_code.click)  # нажатие <Enter>


        # настрйока кнопки входа
        self.ui.btn_login.clicked.connect(lambda: self.check_data())
        self.ui.btn_accept_code.clicked.connect(lambda: self.login_into_system())
        self.ui.btn_registrarion.clicked.connect(lambda: self.show_registration_page())
        self.ui.btn_add_new_user_into_system.clicked.connect(lambda: self.add_new_user_into_system())
        self.ui.btn_return_to_login_page.clicked.connect(lambda: self.show_login_page())

        # сварачиваем окно
        self.ui.btn_minimize_window.clicked.connect(lambda: self.showMinimized())

        # свернуть/развернуть окно
        self.ui.btn_restore_window.clicked.connect(lambda: self.restore_or_maximize_window())

        # настройки кнопки выхода
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_close_window.clicked.connect(self.close)

        # настройка кнопок авторизации
        self.ui.btn_open_authorization_page.clicked.connect(lambda: self.show_login_page())
        self.ui.btn_open_authorization_page_2.clicked.connect(lambda: self.show_login_page())

        # кнопка главной страницы
        self.ui.btn_main_page_manual.clicked.connect(lambda: self.show_main_manual())

        # настройка кнопки лицензия
        self.ui.btn_open_license.clicked.connect(lambda: self.show_license())

        # настройка ввода пароля
        self.ui.le_password.setEchoMode(QLineEdit.Password)
        self.ui.le_email_code.setEchoMode(QLineEdit.Password)

        ######################################
        # настройка кнопок модуля антивируса #
        ######################################
        self.ui.btn_antivirus_manual.clicked.connect(lambda: self.show_antivirus_manual())
        self.ui.btn_information_about_system.clicked.connect(lambda: self.show_information_about_system())

        # настройка регистрации активности
        self.activity_registration_thread = ActivityRegistrationThread()
        self.activity_registration_thread.signal.connect(self.insert_activity_registration_value)
        self.ui.btn_activity_registration.clicked.connect(lambda: self.show_activity_registration_page())

        # настройка проверки файла
        self.ui.progressBar.hide()
        # self.check_file_thread = CheckFileThread()
        self.ui.btn_check_file.clicked.connect(self.show_vulnerability_scanner_page)
        self.ui.btn_start_file_checking.clicked.connect(self.get_variant_of_the_check)
        # # self.check_file_thread.signal.connect(self.insert_check_file_value)
        # # self.ui.btn_check_file.clicked.connect(self.show_check_file)
        # # self.ui.btn_start_file_checking.clicked.connect(lambda: self.select_and_start_check_thread())

        self.check_files_thread = CheckFilesThread()
        self.check_files_thread.signal.connect(self.insert_check_file_value)
        self.ui.btn_start_file_checking.clicked.connect(self.start_full_check)

        # блокировка usb
        self.usb_blocking_thread = CheckUsbThread()
        self.usb_blocking_thread.signal.connect(self.insert_info_about_blocking_usb)
        self.ui.btn_check_usb.clicked.connect(lambda: self.show_usb_block())
        self.ui.btn_allow_usb.clicked.connect(lambda: self.get_allowed_usb())

        # настройка порт сканер
        self.port_scanner_thread = PortScannerThread(self.ui.comboBox_port_scanner.currentText())
        self.port_scanner_thread.signal.connect(self.insert_value)
        self.ui.btn_start_port_scanner.clicked.connect(self.start_port_scanner_thread)
        self.ui.btn_port_scaner.clicked.connect(lambda: self.show_port_scanner())

        # настройка межсетевого экрана
        self.ui.btn_firewall.clicked.connect(self.show_firewall_page)
        self.ui.btn_update_info_about_connections.clicked.connect(lambda: self.update_info_about_connections())

        ######################################
        # настройка кнопок модуля сервер     #
        ######################################
        self.server_thread = ServerThread()
        self.server_thread.signal.connect(self.insert_server_value)
        self.ui.btn_show_info_server.clicked.connect(self.start_show_info)
        self.ui.btn_server_manual.clicked.connect(self.show_server_manual_page)
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

        # отобразить данные из бд
        self.dataModel = QSqlTableModel()
        self.dataModel.setTable("должностные лица")
        self.dataModel.select()
        self.ui.data_table_view.setModel(self.dataModel)

        # растягиваем таблицу по всей ширине
        header = self.ui.data_table_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # поиск записей в базе данных
        self.searchModel = QSqlQueryModel(self)
        self.searchModel.setQuery("""SELECT * FROM `должностные лица`;""")
        self.ui.search_table_view.setModel(self.searchModel)
        self.ui.le_search_data_in_db.textEdited.connect(self.search_user_in_db)

        # зменение записей в базе данных
        self.changeModel = QSqlTableModel(self)
        self.changeModel.setTable("должностные лица")
        self.changeModel.select()
        self.ui.change_table_view.setModel(self.changeModel)
        self.changeModel.beforeUpdate.connect(self.onmodificarModel_beforeUpdate)

        # удаление записей из БД
        self.deleteModel = QSqlTableModel(self)
        self.deleteModel.setTable("должностные лица")
        self.deleteModel.select()
        self.ui.delete_table_view.setModel(self.deleteModel)
        self.ui.delete_table_view.setEditTriggers(QTableView.NoEditTriggers)
        self.ui.delete_table_view.setSelectionBehavior(QTableView.SelectRows)
        self.ui.delete_table_view.clicked.connect(self.delete_user_from_db)

        # открыть список доступных баз данных
        self.ui.btn_open_list_of_db.clicked.connect(lambda: self.open_page_list_of_db())

        # растягиваем таблицу по всей ширине
        db_header = [self.ui.data_table_view, self.ui.search_table_view, self.ui.change_table_view, self.ui.delete_table_view]
        for header in db_header:
            item = header.horizontalHeader()
            item.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        ###############################################
        # настройка кнопок модуля журнала логирования #
        ###############################################
        self.ui.btn_open_action_log.clicked.connect(self.show_logs_and_get_logs)
        self.ui.btn_action_log_manual.clicked.connect(self.show_action_log_manual)

        ###############################################
        # запуск компонентов при старте программы     #
        ###############################################
        self.start_activity_registration_thread() # запуск отслеживания процессов
        self.insert_information_about_usb() # запуск блокировки флешки
        self.start_systemwatch_thread() # запуск лоигрвоания операционной системы

        # растяжение окна
        QSizeGrip(self.ui.size_grip)

        # перетаскиваем окно за шапку
        self.ui.frame.mouseMoveEvent = self.moveWindow

    # перетаскивание окна
    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.oldPos)
                self.oldPos = event.globalPos()
                event.accept()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    # изменение размера окна
    def restore_or_maximize_window(self):
        # если окно на максимум
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

        # открыть страницу авторизации
    def show_login_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.authorization_page)

    # получаем данных
    def get_data(self):
        __login = self.ui.le_login.text()
        __password = self.ui.le_password.text()
        if len(__login) == 0 or len(__password) == 0:
            QtWidgets.QMessageBox.information(self, "Уведомление", "Поля ввода не должны быть пустыми!")
            return False
        else:
            return __login, __password

    # генерируем код для отправки
    def generate_code(self):
        code = self.two_factor_authentication.generate_code()
        return code

    # проверка данных
    def check_data(self):
        global code_from_email
        code_from_email = self.two_factor_authentication.generate_code()
        login_from_form, password_from_form = self.get_data()
        db_users = {}
        model = QSqlQueryModel()
        data = login_from_form
        model.setQuery("SELECT * FROM `должностные лица` WHERE name LIKE '%" + data + "%';") # делаем запрос с логином из поля ввода
        for i in range(5): # при помощи получаем его данные
            user_id = model.record(i).value("user_id")
            login = model.record(i).value("login")
            password = model.record(i).value("password")
            email = model.record(i).value("email")
            if user_id != None and login != None and password != None and email != None:
                db_users[user_id] = [login, password, email] # создаём словарь из его данных
        if len(db_users) > 0:
            for key, value in db_users.items(): # проходим циклом по этому словарю
                login_from_db = value[0]
                password_from_db = value[1]
                email_from_db = value[2]
                if login_from_form == login_from_db and password_from_form == password_from_db: # сравниваем данные из словаря и из полей ввода
                    self.two_factor_authentication.send_email(email=email_from_db, code=code_from_email) # отправляем письмо на почту
                    self.ui.stackedWidget.setCurrentWidget(self.ui.two_factor_authentication_page) # открываем окно с подтверждением кода
                    self.ui.le_login.clear()
                    self.ui.le_password.clear()
        else:
            QtWidgets.QMessageBox.information(self, "Уведомление", "Неверный логин или пароль!")

    # двухфакторная аутентификация
    def start_two_factor_authentication(self):
        code_from_le = self.ui.le_email_code.text()
        if code_from_le == code_from_email:
            return True
        else:
            QtWidgets.QMessageBox.information(self, "Уведомление", "Неверный код!")
            # code_from_le.setEchoMode(QLineEdit.Password)

    # вход в систему
    def login_into_system(self):
        res = self.start_two_factor_authentication()
        if res:
            self.ui.stackedWidget.setCurrentWidget(self.ui.main_container_page)
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_system)
            self.ui.le_email_code.clear()

    # регистрация в системе
    def show_registration_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.add_new_user_page)

    # добавляем новых пользователей в систему
    def add_new_user_into_system(self):
        name = self.ui.le_name_new_user.text()
        soname = self.ui.le_soname_new_user.text()
        position = self.ui.le_position_new_user.text()
        email = self.ui.le_email_new_user.text()
        login = self.ui.le_login_new_user.text()
        password = self.ui.le_password_new_user.text()
        access_level = self.ui.cb_role_new_user.currentText()

        data = {}
        data["name"] = name
        data["soname"] = soname
        data["position"] = position
        data["email"] = email
        data["login"] = login
        data["password"] = password
        data["access_level"] = access_level

        for key in data:
            if data.get(key) == "":
                QtWidgets.QMessageBox.critical(self, "ERROR", "Поля ввода не должны быть пустыми!")
                return

        # access_level = int(access_level)
        query = QSqlQuery()
        insert_query = self.customs_officers_database.insert_data_into_db()
        if query.prepare(insert_query):
            query.addBindValue(name)
            query.addBindValue(soname)
            query.addBindValue(position)
            query.addBindValue(email)
            query.addBindValue(login)
            query.addBindValue(password)
            query.addBindValue(access_level)
            if query.exec_():
                QtWidgets.QMessageBox.information(self, "Уведомление", "Данные успешно добавлены!")
                self.register_actions.register_database_actions("Добавление данных")
                self.ui.le_name.clear()
                self.ui.le_soname.clear()
                self.ui.le_position.clear()
                self.ui.le_email.clear()
                self.ui.le_login_2.clear()
                self.ui.le_password_2.clear()
                self.ui.cb_user_role.clear()
                self.refreshTable()  # обновляем базу данных

    # открыть страницу с информацией о системе
    def show_main_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_system)

    # открыть страницу с лицензией
    def show_license(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_license)

    ########################
    # РАБОТА С АНТИВИРУСОМ #
    ########################
    def show_antivirus_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_antivirus)

    def show_vulnerability_scanner_page(self):
        """открыть страницу сканера файлов"""
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_check_file)

    def get_variant_of_the_check(self):
        """почаем информацию о выборе проверки"""
        fast_check = self.ui.cb_fast_check.isChecked()
        full_check = self.ui.cb_full_check.isChecked()
        if fast_check:
            self.ui.btn_start_file_checking.setEnabled(False)
            self.ui.te_res_of_fast_check.clear()
            self.ui.te_res_of_fast_check.append("Запуск быстрой проверки файлов")
            self.start_fast_check()
            self.start_progress_bar()
        elif full_check:
            self.ui.btn_start_file_checking.setEnabled(False)
            self.ui.te_res_of_full_check.clear()
            self.ui.te_res_of_full_check.append("Запуск полной проверки файлов")
            self.start_progress_bar()
            thread = threading.Thread(target=self.start_full_check)
            thread.start()
            thread.join()
        elif full_check and fast_check:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Необходимо выбрать только один вариант проверки файлов")
        else:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Необходимо выбрать один из вариантов проверки файлов")

    def start_fast_check(self):
        """запускаем быструю проверку файла через локульную бауз данных"""
        # thread = threading.Thread(target=self.antivirus_engine.md5_hash_checker)
        # thread.start()
        thread_pool = ThreadPool()
        thread_res = thread_pool.apply_async(self.antivirus_engine.md5_hash_checker)
        thread_res.get()

    def start_full_check(self):
        """запускаем полную проверку файла через облако"""
        self.check_files_thread.start()

    def insert_check_file_value(self, value):
        self.ui.te_res_of_full_check.append(value)

    ##########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ С РЕГИСТРАЦИЕЙ АКТИВНОСТИ #
    ##########################################################
    def show_activity_registration_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_registration_activity)

    def insert_activity_registration_value(self, value):
        self.ui.lw_activity_registration.addItem(value)

    def start_activity_registration_thread(self):
        self.activity_registration_thread.start()

    #########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ С ПРОВЕРКОЙ ФАЙЛА        #
    #########################################################
    # прогресс бар
    def show_check_file(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_check_file)

    def start_progress_bar(self):
        self.calc = ThreadProgressBar()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.ui.progressBar.setValue(value)
        if value == 100:
            time.sleep(1)
            self.ui.progressBar.hide()

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
        self.ui.lw_of_locked_usb.addItem(value)

    def get_allowed_usb(self):
        self.ui.le_get_usb.clear()
        usb_name = self.ui.le_get_usb.text()
        self.ui.lw_allowed_usb.addItem(usb_name)

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

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ БЛОКИРОВКИ IP #
    ##############################################
    def show_firewall_page(self):
        self.ui.lw_incoming_connections.clear()
        self.show_locked_connections()
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_firewall)

    # сохраняем заблокированные входящие соединения
    def save_locked_connection(self, value):
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\locked_connections.txt"
        with open(path, "a") as file:
            file.write(value)

    # показываем заблокированные входящие соединения
    def show_locked_connections(self):
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\locked_connections.txt"
        with open(path, "r") as file:
            res = file.readlines()
            if len(res) > 0:
                for i in res:
                    self.ui.lw_locked_connections.addItem(str(i))
            else:
                pass

    # блокируем
    def on_connection_item_clicked(self, item):
        self.ui.lw_locked_connections.clear()
        connection = item.text()
        if QtWidgets.QMessageBox.question(self, "Уведомление", "Вы уверены, что хотите заблокировать соединение",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\locked_connections.txt"
            with open(path, "r") as file:
                res = file.readlines()
                if connection in res:
                    QtWidgets.QMessageBox.information(self, "Уведомление",
                                                      "Соединение уже заблокировано!")
                else:
                    self.ui.lw_locked_connections.addItem(connection)

    # обновляем информцию о заблокированных соединениях
    def update_info_about_connections(self):
        self.ui.lw_incoming_connections.clear()
        self.ui.lw_locked_connections.clear()
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\locked_connections.txt"
        with open(path, "r") as file:
            res = file.readlines()
            if len(res) > 0:
                for item in res:
                    self.ui.lw_locked_connections.addItem(str(item))
            else:
                pass
        res_about_connections = self.server.return_info_about_connections()
        if len(res_about_connections) > 0:
            for item in res_about_connections:
                self.ui.lw_incoming_connections.addItem(str(item) + "\n")
                self.save_locked_connection(str(item) + "\n")
        else:
            pass
        self.ui.lw_incoming_connections.itemClicked.connect(self.on_connection_item_clicked)

    ##########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ ЛОГИРОВАНИЯ ОПЕРАЦИОННОЙ СИСТЕМЫ #
    ##########################################################
    def start_systemwatch_thread(self):
        thread = threading.Thread(target=self.system_watch.main)
        thread.start()

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ С СЕРВЕРОМ           #
    ##############################################
    def show_server_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_server_info)

    def show_server_manual_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_server_manual)

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

    # получаем данные и вставляем в таблицу
    def get_data_from_le(self):
        name = self.ui.le_name.text()
        soname = self.ui.le_soname.text()
        position = self.ui.le_position.text()
        email = self.ui.le_email.text()
        login = self.ui.le_login_2.text()
        password = self.ui.le_password_2.text()
        access_level = self.ui.cb_user_role.text()
        # print(name, soname, rank, email, login, password, access_level)

        data = {}
        data["name"] = name
        data["soname"] = soname
        data["position"] = position
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
            query.addBindValue(position)
            query.addBindValue(email)
            query.addBindValue(login)
            query.addBindValue(password)
            query.addBindValue(access_level)
            if query.exec_():
                QtWidgets.QMessageBox.information(self, "Уведомление", "Данные успешно добавлены")
                self.register_actions.register_database_actions("Добавление данных")
                self.ui.le_name.clear()
                self.ui.le_soname.clear()
                self.ui.le_position.clear()
                self.ui.le_email.clear()
                self.ui.le_login_2.clear()
                self.ui.le_password_2.clear()
                self.ui.cb_user_role.clear()
                self.refreshTable()  # обновляем базу данных

    # поиск пользователя в БД
    def search_user_in_db(self, data):
        query = self.customs_officers_database.search_user_from_db(data)
        self.searchModel.setQuery(query)
        self.register_actions.register_database_actions("Поиск данных")

    # удаления пользователя из БД
    def delete_user_from_db(self, idx):
        if QtWidgets.QMessageBox.question(self, "Вопрос", "Вы точно уверены что хотите удалить?",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            row = idx.row()
            if self.deleteModel.removeRow(row):
                self.refreshTable()
                self.register_actions.register_database_actions("Удаление данных")

    # обновление таблицы
    def refreshTable(self):
        self.searchModel.setQuery("""SELECT * FROM `должностные лица`;""")
        self.dataModel.select()
        self.changeModel.select()
        self.deleteModel.select()
        self.register_actions.register_database_actions("Обновление данных")

    def onModificarTimer_timeout(self):
        self.refreshTable()

    def onmodificarModel_beforeUpdate(self, row, record):
        self.refresh_timer.start()

    def show_dbms_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_show_dbms)

    def show_dbms_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_dbms_manual)

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

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ ЖУРНАЛА ЛОГИРОВАНИЯ  #
    ##############################################
    # страница с мануалом по использованию журнала логирования
    def show_action_log_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_show_action_log_manual)

    # страница с доступными журналами
    def show_logs_and_get_logs(self):
        self.ui.lw_log_widget.clear()
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\log_dir"
        dirs = os.listdir(path)
        logs = [file for file in dirs if file.endswith("txt")]
        if len(logs) > 0:
            for log in logs:
                self.ui.lw_log_widget.addItem(log)
        else:
            self.ui.lw_log_widget.addItem("ЖУРНАЛЫ ДЕЙСТВИЙ ОТСУТСТВУЮТ")
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_show_logging_journal)
        self.ui.lw_log_widget.itemClicked.connect(self.onLogClicked)

    # открывает журнал логирования
    def onLogClicked(self, item):
        self.ui.pte_log_action.clear()
        file = item.text()
        path = f"C:\\PycharmProjects\\Antivirus\\dependencies\\log_dir\\{file}"
        with open(path, "r", encoding="utf-8") as file:
            res = file.readlines()
            for i in res:
                self.ui.pte_log_action.appendPlainText(i)


def prepareDatabase():
    db = QSqlDatabase().addDatabase("QSQLITE")
    # db.setDatabaseName(self.dependencies_path+db_name)
    db.setDatabaseName("C:\\PycharmProjects\\Antivirus\\dependencies\\database_dir\\должностные лица домена.db")
    if db.open():
        query = QSqlQuery()
        if query.prepare("""
        CREATE TABLE IF NOT EXISTS `должностные лица` (
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
