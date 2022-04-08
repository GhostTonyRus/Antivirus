import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QDesktopWidget
from system_gui import Ui_MainWindow
from antivirus_package import InfoSystem, PortScanner, Monitor, UsbLock
import time


class ActivityRegistrationThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ActivityRegistrationThread, self).__init__()
        self.monitor = Monitor("creation")

    def run(self):
        self.monitor.main()
        while True:
            time.sleep(3)
            try:
                with open("C:\\PycharmProjects\\Antivirus\\antivirus_package\\activity_registratiom.txt") as file:
                    res = file.readlines()
                    for i in res:
                        self.signal.emit(str(i))
            except FileExistsError as err:
                self.signal.emit("НЕТ ДАННЫХ!")


class PortScannerThread(QtCore.QThread):

    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(PortScannerThread, self).__init__()
        self.port_scanner = PortScanner()

    def run(self):
        res = self.port_scanner.main()
        self.signal.emit(res)


class CheckUsbThread(QtCore.QThread):

    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(CheckUsbThread, self).__init__()
        self.check_usb = UsbLock()

    def run(self):
        ...

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.info = InfoSystem()
        self.port_scaner = PortScanner()

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
        self.ui.btn_end_activity_registration.clicked.connect(lambda: self.end_activity_registration_thread())

        # настройка порт сканер
        self.port_scanner_thread = PortScannerThread()
        self.port_scanner_thread.signal.connect(self.insert_value)
        self.ui.btn_start_port_scanner.clicked.connect(self.start_port_scanner_thread)
        self.ui.btn_port_scaner.clicked.connect(lambda: self.show_port_scanner())

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

    #########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ С РЕГИСТРАЦИЕЙ АКТИВНОСТИ #
    #########################################################
    def show_activity_registration_page(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_registration_activity)

    def insert_activity_registration_value(self, value):
        self.ui.plainTextEdit_for_activity_registration.appendPlainText(value)

    def start_activity_registration_thread(self):
        self.activity_registration_thread.start()

    def end_activity_registration_thread(self):
        try:
            if self.activity_registration_thread.isRunning():
                self.activity_registration_thread.running = False
        except RuntimeError:
            ...

    #########################################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ С ПРОВЕРКОЙ ФАЙЛА         #
    #########################################################
    def show_check_file(self):
        ...

    def show_information_about_system(self):
        self.ui.listWidget_information_about_system.clear()
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_information_about_system)
        system_info = self.info.main()
        self.ui.listWidget_information_about_system.addItem(system_info)

    def show_check_usb(self):
        ...

    #############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ ПОРТ СКАНЕРА #
    #############################################
    def start_port_scanner_thread(self):
        self.ui.plainTextEdit_port_scanner.appendPlainText("Запуск сканера портов")
        self.port_scanner_thread.start()

    def show_port_scanner(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_port_scaner)

    def insert_value(self, value):
        self.ui.plainTextEdit_port_scanner.appendPlainText(value)
        self.ui.plainTextEdit_port_scanner.appendPlainText("....")

    ##############################################
    # НАСТРОЙКА МЕТОДОВ ДЛЯ РАБОТЫ БЛОКИРОВКИ IP #
    ##############################################
    def IP_block(self):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec_())
