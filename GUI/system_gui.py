# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/system_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 965)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_minimize_window = QtWidgets.QPushButton(self.frame_4)
        self.btn_minimize_window.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_minimize_window.setObjectName("btn_minimize_window")
        self.horizontalLayout_2.addWidget(self.btn_minimize_window)
        self.btn_restore_window = QtWidgets.QPushButton(self.frame_4)
        self.btn_restore_window.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_restore_window.setObjectName("btn_restore_window")
        self.horizontalLayout_2.addWidget(self.btn_restore_window)
        self.btn_close_window = QtWidgets.QPushButton(self.frame_4)
        self.btn_close_window.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_close_window.setObjectName("btn_close_window")
        self.horizontalLayout_2.addWidget(self.btn_close_window)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.authorization_page = QtWidgets.QWidget()
        self.authorization_page.setObjectName("authorization_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.authorization_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.authorization_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(300, 300, 300, 300)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_login = QtWidgets.QPushButton(self.frame_5)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_login.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 2, 1, 1, 1)
        self.le_login = QtWidgets.QLineEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_login.sizePolicy().hasHeightForWidth())
        self.le_login.setSizePolicy(sizePolicy)
        self.le_login.setMinimumSize(QtCore.QSize(0, 40))
        self.le_login.setMaximumSize(QtCore.QSize(16777215, 40))
        self.le_login.setObjectName("le_login")
        self.gridLayout.addWidget(self.le_login, 0, 1, 1, 1)
        self.le_password = QtWidgets.QLineEdit(self.frame_5)
        self.le_password.setMinimumSize(QtCore.QSize(0, 40))
        self.le_password.setMaximumSize(QtCore.QSize(16777215, 50))
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMaximumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.btn_registrarion = QtWidgets.QPushButton(self.frame_5)
        self.btn_registrarion.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_registrarion.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_registrarion.setFont(font)
        self.btn_registrarion.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_registrarion.setObjectName("btn_registrarion")
        self.gridLayout.addWidget(self.btn_registrarion, 3, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.authorization_page)
        self.main_container_page = QtWidgets.QWidget()
        self.main_container_page.setObjectName("main_container_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_container_page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.menu_container = QtWidgets.QFrame(self.main_container_page)
        self.menu_container.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_container.setObjectName("menu_container")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_container)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolBox.setObjectName("toolBox")
        self.page_antivirus_menu = QtWidgets.QWidget()
        self.page_antivirus_menu.setGeometry(QtCore.QRect(0, 0, 260, 558))
        self.page_antivirus_menu.setObjectName("page_antivirus_menu")
        self.splitter = QtWidgets.QSplitter(self.page_antivirus_menu)
        self.splitter.setGeometry(QtCore.QRect(10, 30, 231, 531))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btn_antivirus_manual = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_antivirus_manual.setFont(font)
        self.btn_antivirus_manual.setObjectName("btn_antivirus_manual")
        self.btn_activity_registration = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_activity_registration.setFont(font)
        self.btn_activity_registration.setObjectName("btn_activity_registration")
        self.btn_check_file = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_check_file.setFont(font)
        self.btn_check_file.setObjectName("btn_check_file")
        self.btn_information_about_system = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_information_about_system.setFont(font)
        self.btn_information_about_system.setObjectName("btn_information_about_system")
        self.btn_check_usb = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_check_usb.setFont(font)
        self.btn_check_usb.setObjectName("btn_check_usb")
        self.btn_port_scaner = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_port_scaner.setFont(font)
        self.btn_port_scaner.setObjectName("btn_port_scaner")
        self.btn_IP_block = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_IP_block.setFont(font)
        self.btn_IP_block.setObjectName("btn_IP_block")
        self.toolBox.addItem(self.page_antivirus_menu, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_2.setObjectName("page_2")
        self.splitter_2 = QtWidgets.QSplitter(self.page_2)
        self.splitter_2.setGeometry(QtCore.QRect(10, 120, 231, 261))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_3.setObjectName("page_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_15.setGeometry(QtCore.QRect(30, 30, 191, 51))
        self.pushButton_15.setObjectName("pushButton_15")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_4.setObjectName("page_4")
        self.toolBox.addItem(self.page_4, "")
        self.horizontalLayout_6.addWidget(self.toolBox)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.menu_container)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_main_page_manual = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_main_page_manual.setFont(font)
        self.btn_main_page_manual.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_main_page_manual.setObjectName("btn_main_page_manual")
        self.verticalLayout_5.addWidget(self.btn_main_page_manual)
        self.btn_exit = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_5.addWidget(self.btn_exit)
        self.verticalLayout_4.addWidget(self.frame_9, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_5.addWidget(self.menu_container)
        self.frame_7 = QtWidgets.QFrame(self.main_container_page)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.frame_7)
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_about_system = QtWidgets.QWidget()
        self.page_about_system.setObjectName("page_about_system")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_about_system)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.page_about_system)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.verticalLayout_7.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        self.frame_10 = QtWidgets.QFrame(self.page_about_system)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textEdit = QtWidgets.QTextEdit(self.frame_10)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_9.addWidget(self.textEdit)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.stackedWidget_main.addWidget(self.page_about_system)
        self.page_usb_lock = QtWidgets.QWidget()
        self.page_usb_lock.setObjectName("page_usb_lock")
        self.stackedWidget_main.addWidget(self.page_usb_lock)
        self.page_registration_activity = QtWidgets.QWidget()
        self.page_registration_activity.setObjectName("page_registration_activity")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_registration_activity)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_13 = QtWidgets.QFrame(self.page_registration_activity)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lv_activity_registrariob = QtWidgets.QListView(self.frame_13)
        self.lv_activity_registrariob.setObjectName("lv_activity_registrariob")
        self.verticalLayout_14.addWidget(self.lv_activity_registrariob)
        self.verticalLayout_13.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.page_registration_activity)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_start_activity_registration = QtWidgets.QPushButton(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start_activity_registration.setFont(font)
        self.btn_start_activity_registration.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_start_activity_registration.setObjectName("btn_start_activity_registration")
        self.horizontalLayout_7.addWidget(self.btn_start_activity_registration)
        self.btn_end_activity_registration = QtWidgets.QPushButton(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_end_activity_registration.setFont(font)
        self.btn_end_activity_registration.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_end_activity_registration.setObjectName("btn_end_activity_registration")
        self.horizontalLayout_7.addWidget(self.btn_end_activity_registration)
        self.verticalLayout_13.addWidget(self.frame_14, 0, QtCore.Qt.AlignBottom)
        self.stackedWidget_main.addWidget(self.page_registration_activity)
        self.page_about_antivirus = QtWidgets.QWidget()
        self.page_about_antivirus.setObjectName("page_about_antivirus")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_about_antivirus)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_11 = QtWidgets.QFrame(self.page_about_antivirus)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_11, 0, QtCore.Qt.AlignTop)
        self.frame_12 = QtWidgets.QFrame(self.page_about_antivirus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_12)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_12.addWidget(self.textEdit_2)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.stackedWidget_main.addWidget(self.page_about_antivirus)
        self.page_information_about_system = QtWidgets.QWidget()
        self.page_information_about_system.setObjectName("page_information_about_system")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_information_about_system)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_15 = QtWidgets.QFrame(self.page_information_about_system)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.frame_15.setFont(font)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.listWidget_information_about_system = QtWidgets.QListWidget(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_information_about_system.setFont(font)
        self.listWidget_information_about_system.setStyleSheet("color: rgb(255, 255, 255);")
        self.listWidget_information_about_system.setObjectName("listWidget_information_about_system")
        self.verticalLayout_16.addWidget(self.listWidget_information_about_system)
        self.verticalLayout_15.addWidget(self.frame_15)
        self.stackedWidget_main.addWidget(self.page_information_about_system)
        self.page_port_scaner = QtWidgets.QWidget()
        self.page_port_scaner.setObjectName("page_port_scaner")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_port_scaner)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_16 = QtWidgets.QFrame(self.page_port_scaner)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.listWidget_port_scaner = QtWidgets.QListWidget(self.frame_16)
        self.listWidget_port_scaner.setObjectName("listWidget_port_scaner")
        self.verticalLayout_18.addWidget(self.listWidget_port_scaner)
        self.verticalLayout_17.addWidget(self.frame_16)
        self.stackedWidget_main.addWidget(self.page_port_scaner)
        self.verticalLayout_6.addWidget(self.stackedWidget_main)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.main_container_page)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "НАЗВАНИЕ ПРОГРАММЫ"))
        self.btn_minimize_window.setText(_translate("MainWindow", "-"))
        self.btn_restore_window.setText(_translate("MainWindow", "="))
        self.btn_close_window.setText(_translate("MainWindow", "X"))
        self.btn_login.setText(_translate("MainWindow", "ВОЙТИ"))
        self.label_2.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_3.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.btn_registrarion.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.btn_antivirus_manual.setText(_translate("MainWindow", "Мануал"))
        self.btn_activity_registration.setText(_translate("MainWindow", "Отслеживание процессов"))
        self.btn_check_file.setText(_translate("MainWindow", "Проверка файла"))
        self.btn_information_about_system.setText(_translate("MainWindow", "Информация о системе"))
        self.btn_check_usb.setText(_translate("MainWindow", "Проверка USB"))
        self.btn_port_scaner.setText(_translate("MainWindow", "Сканер портов"))
        self.btn_IP_block.setText(_translate("MainWindow", "Блокировка IP"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_antivirus_menu), _translate("MainWindow", "Антивирус"))
        self.pushButton_13.setText(_translate("MainWindow", "Запуск сервера"))
        self.pushButton_14.setText(_translate("MainWindow", "Остановка сервера"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Сервер"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "СУБД"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Журнал действий"))
        self.btn_main_page_manual.setText(_translate("MainWindow", "Главная страница"))
        self.btn_exit.setText(_translate("MainWindow", "ВЫХОД"))
        self.label_4.setText(_translate("MainWindow", "Информация о системе"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Будущая информация о системе</span></p></body></html>"))
        self.btn_start_activity_registration.setText(_translate("MainWindow", "Старт"))
        self.btn_end_activity_registration.setText(_translate("MainWindow", "Стоп"))
        self.label_5.setText(_translate("MainWindow", "Мануал"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Первый пакет – Antivirus package. В данном пакете находятся модули, для обеспечения следующего функционала:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Идентификация и аутентификация. Данный модуль предоставляет функционал для входа в Систему. Модуль содержит: аутентификацию. Должностное лицо, должно войти в систему при по-мощи логина и пароля. идентификацию. Систему сверяется с введёнными данными. Если введённые данные верны, то пользователю должностное лицо подтвердить вход по e-mail адресу. После успешной идентификации приходит письмо с кодом для входа в Систему. В дальнейшем планируется возможность получения кода по номеру телефона.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Отслеживание процессов. Данный модуль позволяет отслеживать процессы, для выявления вирус-ной активности и следить за системными ресурсами.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Проверка файла. В данный модуль можно загрузить файл и получить всю информацию о нём, а также узнать содержит ли этот файл вредоносный код. Во время разработки возможно добавление нового функционала или от-каз от ненужного.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Сбор информации о системе. Данный модуль позволяет узнать более точную информацию об операционной системе на которой установлена Система.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Проверка USB.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Сканер портов. Данный модуль предоставляет функционал для поиска открытых портов IP-адреса, на котором располагается сервер. Сканирование портов может по-мочь определить потенциальные цели атаки, а также выяснить какие порты открыты, закрыты и используются операционной системой.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\">Блокирвока IP-адресов</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:8pt; color:#c9d1d9;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:8pt; color:#c9d1d9;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:8pt; color:#c9d1d9;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:8pt; color:#c9d1d9;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:8pt; color:#c9d1d9;\"><br /></p></body></html>"))
import icons_rc
