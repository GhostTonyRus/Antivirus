import os
from datetime import datetime


class Logging:

    def __init__(self, name_of_the_system=""):
        self.name_of_the_system = name_of_the_system
        self.name_of_the_system_logger = name_of_the_system + "_log" + ".txt"
        self.log_directory = os.getcwd()
        self.__msg_datetime = datetime.today()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%m-%d-%Y %H:%M:%S')
        self.log_path = "C:\\PycharmProjects\\Antivirus\\dependencies\\log_dir\\"
        print(f"Журнал {self.name_of_the_system_logger} инициализирован для директории {self.name_of_the_system}\n")

        self.MANUAL = """
        +--------------------------------------------------+
        | 1 | посмотреть журнал активности антивируса      |
        +--------------------------------------------------+
        | 2 | посмотреть журнал активности базы данных     |
        +--------------------------------------------------+
        | 3 | посмотреть журнал активности сервера         |
        +--------------------------------------------------+
        | exit/0 | для выхода из модуля журнала активности |
        +--------------------------------------------------+
        """

    # def check_path_file(self):
    #     new_path = ("C:\PycharmProjects\ANTIVIRUS\{}".format(self.name_of_the_system))
    #     os.chdir(new_path)
    #     try:
    #         with open(self.name_of_the_system_logger, "w", encoding="utf-8") as file:
    #             file.write("#"*50+"\n")
    #     except FileExistsError:
    #         raise FileExistsError("Файла не существует!")

    def register_antivirus_action(self, antivirus_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ АНТИВИРУСА"""
        try:
            with open(f"{self.log_path}antivirus_action", "a", encoding="utf-8") as file:
                file.write(f"{antivirus_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError as err:
            return err

    def register_database_actions(self, database_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ БАЗЫ ДАННЫХ"""
        try:
            with open(f"{self.log_path}логирование баз данных.txt", "a", encoding="utf-8") as file:
                file.write(f"{database_action} | {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}\n")
        except FileExistsError:
            raise FileExistsError("Файла не существует")

    def register_server_actions(self, server_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ СЕРВЕРА"""
        try:
            with open(f"{self.log_path}логирование сервера.txt", "a", encoding="utf-8") as file:
                file.write(f"{server_action} | {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}\n")
        except FileExistsError as err:
            return err

    def register_os_system_action(self, os_action, src):
        try:
            with open(f"{self.log_path}логирование операционной системы.txt", "a", encoding="utf-8") as file:
                file.write(f"{os_action} {src} | {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}\n")
        except FileExistsError as err:
            return err

    def register_user_actions(self, user_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЯ"""
        try:
            with open(f"{self.log_path}client_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{user_action} | {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}\n")
        except FileExistsError as err:
            return err

    def get_database_administrator_actions(self, administrator_action):
        """РЕГИСТРИРУЕТ ДЕЙСТВИЯ АДМНИСТРТАОРА БАЗ ДАННЫХ"""
        try:
            with open(f"{self.log_path}дейтсвия администратора баз данных.txt", "a", encoding="utf-8") as file:
                file.write(f"{administrator_action} | {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}\n")
        except FileExistsError as err:
            return err

if __name__ == '__main__':
    # log = Logging("loging")
    # log.get_action()
    files = os.listdir(os.getcwd())
    for file in files:
        if file.endswith("txt"):
            print(file)
