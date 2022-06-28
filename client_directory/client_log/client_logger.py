import os
from datetime import datetime


class Client_logger:
    def __init__(self, name_of_the_system=""):
        self.name_of_the_system = name_of_the_system
        self.name_of_the_system_logger = name_of_the_system + "_log" + ".txt"
        self.log_directory = os.getcwd()
        self.__msg_datetime = datetime.today()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%m-%d-%Y %H:%M:%S')
        self.log_path = "C:\\PycharmProjects\\Antivirus\\client_directory\\dependencies\\log_dir\\"
        print(f"Журнал {self.name_of_the_system_logger} инициализирован для директории {self.name_of_the_system}\n")

    def register_os_system_action(self, os_action, src):
        try:
            with open(f"{self.log_path}логирование операционной системы.txt", "a", encoding="utf-8") as file:
                file.write(f"{os_action} {src} | {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}\n")
        except FileExistsError as err:
            return err

