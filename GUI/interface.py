import sys
import threading
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation, QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QDesktopWidget
from system_gui import Ui_MainWindow
from antivirus_package import InfoSystem, PortScanner, Monitor, UsbLock
from server_package import Server
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
        self.check_usb.main()
        # while True:
        #     try:
        #         with open("C:\\PycharmProjects\\Antivirus\\antivirus_package\\locked_usb.txt", "r", encoding="utf-8") as file:
        #             res = file.readlines()
        #             for i in res:
        #                 self.signal.emit(str(i))
        #     except FileExistsError as err:
        #         self.signal.emit("НЕТ ДАННЫХ!")

class ServerThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ServerThread, self).__init__()
        self.server = Server()

    def run(self):
        self.server.main()
        # while True:
        #     time.sleep(3)
        #     try:
        #         with open("C:\\PycharmProjects\\Antivirus\\logging_package\\server_action.txt", "r") as file:
        #             res = file.readlines()
        #             for i in res:
        #                 self.signal.emit(str(i))
        #     except FileExistsError as err:
        #         self.signal.emit("НЕТ ДАННЫХ!")


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.info = InfoSystem() # информация о системе
        self.usb_blocking = UsbLock() # блокировка usb
        self.port_scanner = PortScanner() # сканер портов
        self.server = Server()

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

        # настрйока конпки входа
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
        # self.ui.btn_end_activity_registration.clicked.connect(lambda: self.end_activity_registration_thread())

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
        # self.server_thread = ServerThread()
        # self.server_thread.signal.connect(self.insert_server_value)
        # self.ui.btn_start_server.clicked.connect(self.start_server_thread)
        self.ui.btn_show_server_page.clicked.connect(lambda: self.show_server_page())

        self.ui.btn_start_server.clicked.connect(self.thread)

    def thread(self):
        t1 = threading.Thread(target=self.server.main)
        t1.start()

    def start_server_thread(self):
        self.server_thread.start()

    def show_server_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_server_info)

    def insert_server_value(self, value):
        self.ui.plainTextEdit_infromation_from_server.appendPlainText(value)

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

    # регистрация в системе
    def registration(self):
        pass

    ########################
    # РАБОТА С АНТИВИРУСОМ #
    ########################
    def show_antivirus_manual(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_about_antivirus)

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
        ...


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
        self.ui.textEdit_usb_blocking.setPlainText(value)

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
    # РАБОТА С СЕРВЕРОМ                          #
    ##############################################
    # def show_server_page(self):
    #     self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_server_info)
    #
    # def start_server_thread(self):
    #     time.sleep(2)
    #     self.server_thread.start()
    #
    # def insert_server_value(self, value):
    #     self.ui.plainTextEdit_infromation_from_server.appendPlainText(value)


    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ С СЕРВЕРОМ           #
    ##############################################



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec_())
