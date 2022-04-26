import hashlib
import json
import os
#############################################
#                   ND5                     #
#############################################


class AntivirusEngine:
    def __init__(self, value):
        self.value = value

    #############################################
    #                   MD5                     #
    #############################################
    def get_md5_hash(self, file_hash):
        with open(file_hash, "rb") as file:
            bytes = file.read()
            md5_hash = hashlib.md5(bytes).hexdigest()
            return md5_hash

    def malware_checker(self, file_hash):
        hash_malware_check = file_hash
        with open("virus_hash.txt", "r") as file:
            hashes = file.read().split()
            for hash in hashes:
                if hash == hash_malware_check:
                    return True
                else:
                    return False

    #############################################
    #                  SHA256                   #
    #############################################
    def get_sha256_hash(self, file_name):
        with open(file_name, "rb") as file:
            bytes = file.read()
            sha256_hash = hashlib.sha256(bytes).hexdigest()
            return sha256_hash

    def check_sha256_file(self, file_hash):
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\SHA256.txt"
        with open(path, "r") as file:
            hashes = file.read().split()
            for hash in hashes:
                if hash == file_hash:
                    return True
                else:
                    return False

    #############################################
    #                  SHA1                     #
    #############################################
    def get_sha1_hash(self, filename):
        with open(filename, "rb") as file:
            res = file.read()
            hash = hashlib.sha1(res).hexdigest()
            return hash


    def check_sha1_file(self, file_hash):
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\SHA1_HASHES.json"
        with open(path, "r") as file:
            res = json.load(file)
            for key, value in enumerate(res["data"]):
                if value["hash"] == file_hash:
                    return True
                else:
                    return False

    def main(self):
        for dirpath, dirnames, filenames in os.walk("C:\\"):
            for filename in filenames:
                file = os.path.abspath(filename)
                if "." not in file:
                    pass
                else:
                    try:
                        with open(rf"{file}", "rb") as file:
                            res = file.read()
                            hash = hashlib.sha1(res).hexdigest()
                            print(check_sha256_file(hash))
                            # print(hash)
                    except FileNotFoundError as err:
                        ...

# main()
# from pathlib import Path
# res = main().split("\\")
# p = Path("\\".join(res))
# with open(p, "rb") as file:
# try:
#     h = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\bootTel.dat"
#     with open(rf"{h}", "rb") as file:
#         res = file.read()
#         hash = hashlib.sha1(res).hexdigest()
#         print(hash)
# except FileNotFoundError as err:
#     ...
# finally:
#     print("dfsf")

import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

TIME_LIMIT = 100


class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def get_dirs(self):
        dirs = []
        # for dirpath, dirnames, filenames in os.walk("C:\\PycharmProjects\\Antivirus"):
        for dirpath, dirnames, filenames in os.walk("C:\\PycharmProjects\\Antivirus"):
            dirs.append(dirnames)
        return dirs

    def run(self):
        dirs = self.get_dirs()
        for i in range(len(dirs)):
            time.sleep(0.01)
            self.ui.progressBar.setProperty("value", i)
            time.sleep(1)
            self.countChanged.emit(i)


class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.button = QPushButton('Start', self)
        self.button.move(0, 30)
        self.show()

        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())
