from PyQt5 import QtWidgets, QtCore, QtGui


class Input_Box(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Input_Box, self).__init__(parent)

        open_message = QtWidgets.QLabel("Enter Value:")
        self.txt = QtWidgets.QLineEdit()
        save = QtWidgets.QPushButton('Save', clicked=self.accept)
        cancel = QtWidgets.QPushButton('Cancel', clicked=self.reject)

        grid = QtWidgets.QGridLayout(self)
        grid.setSpacing(10)
        grid.addWidget(open_message, 0, 0)
        grid.addWidget(self.txt, 1, 0, 1, 2)
        grid.addWidget(save, 2, 0)
        grid.addWidget(cancel, 2, 1)
        self.setFixedSize(self.sizeHint())

    def save(self):
        value = self.txt.text()
        return value


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel("Hello World")
        self.listWidget = QtWidgets.QListWidget()
        addButton = QtWidgets.QPushButton('Add', clicked=self.add_button)

        grid = QtWidgets.QGridLayout(self)
        grid.setSpacing(10)
        grid.addWidget(label)
        grid.addWidget(self.listWidget)
        grid.addWidget(addButton)

    def add_button(self):
        input_box = Input_Box()
        input_box.setWindowTitle("Window 2")
        if input_box.exec_() == QtWidgets.QDialog.Accepted:
            val = input_box.save()
            newButton = QtWidgets.QPushButton(f'{val}')
            newButton.clicked.connect(lambda btn, text=val: self.onClicked(text))

            listWidgetItem = QtWidgets.QListWidgetItem()
            listWidgetItem.setSizeHint(newButton.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, newButton)
            self.listWidget.scrollToItem(listWidgetItem)

    def onClicked(self, text):
        print(text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())