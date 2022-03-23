"""
 __  __    _    ___ _   _
|  \/  |  / \  |_ _| \ | |
| |\/| | / _ \  | ||  \| |
| |  | |/ ___ \ | || |\  |
|_|  |_/_/   \_\___|_| \_|

"""
# from database_package import UsersDataBase, OfficerDatabase
# from antivirus_package import Two_factor_authentication
# class MainScript:
#     def __init__(self):
#         officer_database = OfficerDatabase("customs_officers_database.db")
import threading

from antivirus_package import Two_factor_authentication

class StartProgramm:

    def __init__(self):
        pass

    def hello(self):
        login = input("Введите login\n>>>").strip()
        password = input("Введите пароль:\n>>>").strip()
        self.antivirus_methods = Two_factor_authentication(login, password)  # модуль аутентификации и идентификации
        self.antivirus_methods.login_to_the_system()

    def start_program(self):
        manual = """
        +--------------------------------+
        | 1 | модуль антивируса          |
        +--------------------------------+
        | 2 | модуль базы данных         |
        +--------------------------------+
        | 3 | серверный модуль           |
        +--------------------------------+
        | 4 | модуль логирования         |
        +--------------------------------+
        | exit | для выхода из программы |
        +--------------------------------+
        \n>>>"""
        while True:
            response = str(input(manual))
            if response == "1":
                pass
            elif response == "2":
                pass
            elif response == "3":
                pass
            elif response == "4":
                pass
            elif response == "exit":
                print("Завершение программы")
            else:
                print("Такой цфиры в мануале")

    def start_antivirus_package(self):
        pass

    def start_database_package(self):
        pass

    def start_server_package(self):
        pass

    def start_logging_package(self):
        pass

    def thread_start_func(self, func, args):
        thread = threading.Thread(target=func, args=(args, ))
        thread.start()
        thread.join()

if __name__ == '__main__':
    s_p = StartProgramm()
    s_p.hello()

