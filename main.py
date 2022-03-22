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
from antivirus_package import Two_factor_authentication

class StartProgramm:

    def __init__(self):
        pass

    def hello(self):
        login = input("Введите login\n>>>").strip()
        password = input("Введите пароль:\n>>>").strip()
        self.antivirus_methods = Two_factor_authentication(login, password)  # модуль аутентификации и идентификации
        self.antivirus_methods.login_to_the_system()

if __name__ == '__main__':
    s_p = StartProgramm()
    s_p.hello()

