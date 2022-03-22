import os
from datetime import datetime


class Logging:

    def __init__(self, name_of_the_system):
        self.name_of_the_system = name_of_the_system
        self.name_of_the_system_logger = name_of_the_system + "_log" + ".txt"
        self.log_directory = os.getcwd()
        self.__msg_datetime = datetime.now()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.log_path = "C:\\PycharmProjects\\Antivirus\\logging_package"
        print(f"Журнал {self.name_of_the_system_logger} инициализирован для директории {self.name_of_the_system}\n")

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
            with open(f"{self.log_path}\\antivirus_action", "a", encoding="utf-8") as file:
                file.write(f"{antivirus_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError as err:
            return err

    def register_database_actions(self, database_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ БАЗЫ ДАННЫХ"""
        try:
            with open(f"{self.log_path}\\database_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{database_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError:
            raise FileExistsError("Файла не существует")

    def register_server_actions(self, server_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ СЕРВЕРА"""
        try:
            with open(f"{self.log_path}\\server_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{server_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError as err:
            return err

    def register_user_actions(self, user_action):
        """ЖУРНАЛ ЛОГИРВОАНИЯ ДЛЯ ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЯ"""
        try:
            with open(f"{self.log_path}\\client_action.txt", "a", encoding="utf-8") as file:
                file.write(f"{user_action} | {self.__custom_msg_datetime}\n")
        except FileExistsError as err:
            return err

    def get_actions(self):
        pass

if __name__ == '__main__':
    print(os.getcwd())
    with open("text.txt", "w") as file:
        file.write("hello world")