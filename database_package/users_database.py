from database_package.base_database_model import DataBaseClass
import os
from datetime import datetime
import sqlite3
from sqlite3 import Error
from logging_package import Logging

class UsersDataBase:
    __logger = Logging("database_package")  # журнал логирования

    def __init__(self, database_name=None):
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.database_name = database_name
        self.__path = "../dependencies/database_dir/пользователи домена.db"
        self.connection = sqlite3.connect(self.__path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """метод для создания таблицы в базде данных"""
        with self.connection:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `пользователи` (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Имя TEXT,
                Фамилия TEXT,
                Отчество TEXT,
                Должность TEXT,
                Отдел TEXT,
                Email TEXT,
                Логин TEXT,
                Пароль TEXT,
                Уровень_доступа TEXT);""")

    def insert_data_into_table(self, *args):
        """метод для добавления данных в таблицу)"""
        with self.connection:
            self.cursor.execute(
            """
                INSERT INTO
                   `пользователи` (Имя, Фамилия, Отчество, Должность, Отдел, Email, Логин, Пароль, Уровень_доступа)
                VALUES (
                    '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(*args)
            )

    def get_data_from_table(self, data):
        """метод для получения данных из таблицы"""
        new_users_data = {}
        with self.connection:
            for key, value in data.items():
                self.cursor.execute("""
                SELECT Логин, Пароль FROM `пользователи` WHERE Логин LIKE '{}';
                """.format(key))
            res_from_db = self.cursor.fetchone()
            new_users_data[res_from_db[0]] = res_from_db[1]

        # сравниваем полученные данные от пользователя и выборкой из бд
        for login_from_db, password_from_db in new_users_data.items():
            for login, password in data.items():
                if login_from_db == login and password_from_db == password:
                    return True
                else:
                    return False

        # self.__logger.register_database_actions(
        #     "получаем данные из таблицы customs_users"
        # )

    def update_data_in_table(self, table_name: str, id: int, row: str, value: str):
        """метод для обновления данных в таблице"""
        try:
            with self.connection:
                self.cursor.execute(f"""
                UPDATE `{table_name}` SET {row} = {value} WHERE user_id = {id}""")
                self.connection.commit()
                self.__logger.register_database_actions(
                    f"данные обновлены в таблицу {table_name}"
                )
        except Error as err:
            ...
            # logger.error(err)

    def delete_data_from_table(self, table_name: str, id: int):
        """метод для удаления данных из таблицы"""
        try:
            with self.connection:
                self.cursor.execute(f"""
                DELETE FROM `{table_name}` WHERE user_id = {id}""")
                self.connection.commit()
                self.__logger.register_database_actions(
                    f"удаление данных из таблицы {table_name}"
                )
        except Error as err:
            ...
            # logger.error(err)

    def drop_table(self, table_name: str):
        """метод для удаления таблци из бащы данных"""
        try:
            with self.connection:
                self.cursor.execute(f"""
                DROP TABLE IF EXISTS `{table_name}`""")
                self.connection.commit()
                self.__logger.register_database_actions(
                    f"таблица {table_name} удалена"
                )
        except Error as err:
            ...
            # logger.error(err)

    def delete_database(self, database_name: str):
        """метод дя удаления базы данных"""
        self.database_name = database_name
        self.connection.close()
        try:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self.database_name)
            if path:
                os.remove(path)
                self.__logger.register_database_actions(
                    f"база данных {database_name} удалена"
                )
        except PermissionError as err:
            ...
            # logger.debug(err)




if __name__ == '__main__':
    users = UsersDataBase()
    print(users.get_data_from_table({"MakeevAN": "12345"}))
    # # print(users.get_data_from_table({"antonmakeev18@gmail.com": "12345"}))
    # # path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"
    # with sqlite3.connect("../dependencies/database_dir/пользователи домена.db") as db:
    #     cur = db.cursor()
    #     cur.execute(
    #         """SELECT * FROM `пользователи`;"""
    #     )
    #     print(cur.fetchall())
