import os
from datetime import datetime


class Logging:

    def __init__(self, name_of_the_system):
        self.name_of_the_system = name_of_the_system
        self.name_of_the_system_logger = name_of_the_system + "_log" + ".txt"
        self.log_directory = os.getcwd()
        self.__msg_datetime = datetime.now()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.log_path = "C:\\PycharmProjects\\Antivirus\\logging_package\\"
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
            with open(f"{self.log_path}database_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{database_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError:
            raise FileExistsError("Файла не существует")

    def register_server_actions(self, server_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ СЕРВЕРА"""
        try:
            with open(f"{self.log_path}server_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{server_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError as err:
            return err

    def register_user_actions(self, user_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЯ"""
        try:
            with open(f"{self.log_path}client_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{user_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError as err:
            return err

    def get_action(self):
        """ВЫВОДИМ ДАННЫЕ ИЗ ЖУРНАЛА ЛОГИРОВАНИЯ"""
        print(self.MANUAL)
        modules_dict = {
            "1": f"{self.log_path}server_action.txt",
            "2": f"{self.log_path}database_action.txt",
            "3": f"{self.log_path}server_action.txt",
        }
        while True:
            response = input(">>> ")
            if response == "exit":
                print("Выход из модуля журнала активности!")
                break
            elif response:
                try:
                    with open(modules_dict.get(str(response)), "r", encoding="utf-8") as file:
                        res = file.readlines()
                        for i in res:
                            print(i)
                except FileExistsError as err:
                    print(err)

if __name__ == '__main__':
    log = Logging("loging")
    log.get_action()

