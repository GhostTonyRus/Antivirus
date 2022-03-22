import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QPoint, QPropertyAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QDesktopWidget

from  GUI.test_ui import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # удаляем заголовок
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # делаем главный экран прозрачным
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # эффект тени
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        # применяем тень к центральному виджету
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # устанавливаем иконку
        self.setWindowIcon(QtGui.QIcon(u"C:\\PycharmProjects\\Antivirus\\GUI\\icons\\github.svg"))

        # устанавливаем загаловок
        self.setWindowTitle("MODERN UI")

        # захват размера окна для изменения размера окна
        QSizeGrip(self.ui.size_grip)

        # сварачиваем окно
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        # закрываем окно
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        # развернуть/свернуть окно
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_pr_maximize_window())

        # открыть/закрыть оковое меню
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())

        self.show()

    def slideLeftMenu(self):
        # left_menu_cont_frame
        width = self.ui.side_menu_container.width()
        if width == 0:
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(
                QtGui.QIcon(u"C:\\PycharmProjects\\Antivirus\\GUI\\icons\\chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(
                QtGui.QIcon(u"C:\\PycharmProjects\\Antivirus\\GUI\\icons\\align-left.svg"))

        self.animation = QPropertyAnimation(self.ui.side_menu_container, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

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
    def restore_pr_maximize_window(self):
        # если окно на максимум
        if self.isMaximized():
            self.showNormal()
            # меняем иконку
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u"C:\\PycharmProjects\\Antivirus\\GUI\\icons\\maximize-2.svg"))
        else:
            self.showMaximized()
            # меняем иконку
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u"C:\\PycharmProjects\\Antivirus\\GUI\\icons\\minimize-2.svg"))


if __name__ == '__main__':
    # pyrcc5 GUI/icons.qrc -o icons_rc.py чтобы заработали иконки
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())

