"""
 __  __    _    ___ _   _
|  \/  |  / \  |_ _| \ | |
| |\/| | / _ \  | ||  \| |
| |  | |/ ___ \ | || |\  |
|_|  |_/_/   \_\___|_| \_|

"""
######################################################
# MODULES
######################################################
import threading
from antivirus_package import Two_factor_authentication
from antivirus_package import Antivirus
from database_package import DataBaseMain
from server_package import Server
from logging_package import Logging

class StartProgramm:

    def __init__(self):
        pass

    def hello(self):
        login = input("Введите login\n>>>").strip()
        password = input("Введите пароль:\n>>>").strip()
        self.antivirus = Antivirus() # класс антивируса
        self.database = DataBaseMain()
        self.server = Server()
        self.logger = Logging("main_script")
        # self.antivirus_methods = Two_factor_authentication(login, password)  # модуль аутентификации и идентификации
        # self.antivirus_methods.login_to_the_system()


    def start_program(self):
        manual = """
        +----------------------------------+
        | 1 | модуль антивируса            |
        +----------------------------------+
        | 2 | модуль базы данных           |
        +----------------------------------+
        | 3 | серверный модуль             |
        +----------------------------------+
        | 4 | модуль логирования           |
        +----------------------------------+
        | exit/0 | для выхода из программы |
        +----------------------------------+
        \n>>>"""
        while True:
            response = str(input(manual))
            if response == "1":
                self.start_thread_antivirus_package()
            elif response == "2":
                self.start_thread_database_package()
            elif response == "3":
                pass
            elif response == "4":
                self.start_logging_package()
            elif response == "exit" or response == "0":
                print("Завершение программы")
                break
            else:
                print("Такой цифры в мануале")

    def start_thread_antivirus_package(self):
        thread = threading.Thread(target=self.antivirus.main)
        thread.start()
        thread.join()

    def start_thread_database_package(self):
        """ЗАПУСК РАБОТЫ ПАКЕТА БАЗЫДАННЫХ В ПОТОК"""
        therad = threading.Thread(target=self.database.main())
        therad.start()
        therad.join()

    def start_server_package(self):
        """ЗАПУСК РАБОТЫ ПАКЕТА СЕРВЕРА В ПОТОК"""
        thread = threading.Thread(target=self.server.main(("127.0.0.1", 12345), 10))
        thread.start()
        thread.join()

    def start_logging_package(self):
        """ЗАПУСК РАБОТЫ ПАКЕТА ЖУРНАЛА АКТИВНОСТИ В ПОТОК"""
        thread = threading.Thread(target=self.logger.get_action())
        thread.start()
        thread.join()

    def thread_start_func(self, func, args):
        thread = threading.Thread(target=func, args=(args, ))
        thread.start()
        thread.join()

if __name__ == '__main__':
    app = StartProgramm()
    app.hello()
    app.start_program()

