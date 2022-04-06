import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QDesktopWidget
from system_gui import Ui_MainWindow
from antivirus_package import InfoSystem, PortScanner

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
        self.ui.btn_activity_registration.clicked.connect(lambda: self.show_activity_registration())
        self.ui.btn_information_about_system.clicked.connect(self.show_information_about_system)
        self.ui.btn_port_scaner.clicked.connect(lambda: self.port_scanner())

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

    # открыть страницу с информациоей о системе
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

    def show_activity_registration(self):
        ...

    def show_check_file(self):
        ...

    def show_information_about_system(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_information_about_system)
        system_info = self.info.main()
        self.ui.listWidget_information_about_system.addItem(system_info)

    def show_check_usb(self):
        ...

    def port_scanner(self):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_port_scaner)
        port_scanner = self.port_scaner.main()
        self.ui.listWidget_port_scaner.addItem(port_scanner)

    def IP_block(self):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec_())

