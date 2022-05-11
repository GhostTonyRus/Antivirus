import os
from datetime import datetime
import sqlite3
from sqlite3 import Error
from logging_package import Logging

class DataBaseClass:
    __logger = Logging("database_package")  # журнал логирования

    def __init__(self, database_name):
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.database_name = database_name
        self.__path = f"C:\\PycharmProjects\\Antivirus\\database_package\\{self.database_name}.db"
        self.connection = sqlite3.connect(self.__path)
        self.cursor = self.connection.cursor()
        self.MANUAL = """
        +---------------------------------------------------------+
        | 1 | получить таблицы из базы данных                     |
        +---------------------------------------------------------+
        | 2 | создать таблицу (введите название таблиц)           |
        +---------------------------------------------------------+
        | 3 | вставить данные в таблицу                           |
        |   | (название таблиц, данные через запятую:             |
        +---------------------------------------------------------+
        | 4 | получить данные из таблиц (введите название таблиц) |
        +---------------------------------------------------------+
        | 5 | обновить данные в таблице                           |
        +---------------------------------------------------------+
        | 6 | удалить данные из таблицы                           |
        +---------------------------------------------------------+
        | 7 | удалить таблицу (введите название таблиц)           |
        +---------------------------------------------------------+
        | exit/0 | выйти из меню баз данных                       |
        +---------------------------------------------------------+\n"""
        if not self.database_name in os.listdir():
            self.__logger.register_database_actions(
                f"инициализация базы данных {self.database_name} | {self.__custom_datetime}\n")

    def get_tables_from_database(self):
        """метод для получения таблиц из базы данных"""
        try:
            with self.connection:
                self.cursor.execute(f"""
                        SELECT name FROM sqlite_master WHERE type='table';""")
                result = self.cursor.fetchall()
                self.__logger.register_database_actions(
                    f"вывод существующих таблиц из базы данных"
                )
                return "\n" + "\n".join(
                    [table for res in result for table in res])  # получаем список таблиц из базы данных
        except Error as err:
            ...
            # logger.error(err)

    def create_table(self, table_name):
        """метод для создания таблицы в базе данных"""
        pass

    def insert_data_to_table(self, table_name: str, *args):
        """вставляем данные в таблицу"""
        pass

    def get_data_from_table(self, table_name: str):
        """получаем данные из таблицы"""
        pass

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
            return err

    def check_data(self, table_name, login, password):
        """проверяем введённые данные"""
        users = {}
        try:
            with self.connection:
                self.cursor.execute(f"""SELECT 
                                   `login`, `password` 
                                FROM 
                                    `{table_name}` 
                                WHERE 
                                    login = "{login}" AND password = "{password}";""")
                data = self.cursor.fetchall()
                if data:
                    for i in data:
                        users[i[0]] = i[1]
                        for user_login, user_password in users.items():
                            if user_login == login and user_password == password:
                                return True
                            else:
                                return False
        except sqlite3.Error as err:
            print(err)

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

    def delete_data_from_table(self, table_name: str, id: int):
        pass

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
            return err

    @property
    def manual(self):
        return self.MANUAL

    def main(self):
        functions_dict = {
            "1": self.get_tables_from_database,
            "2": self.create_table,
            "3": self.insert_data_to_table,
            "4": self.get_data_from_table,
            "5": self.update_data_in_table,
            "6": self.delete_data_from_table,
            "7": self.drop_table
        }
        while True:
            response = input(">>> ").split()
            command = str(response[0])
            values = response[1:]
            res = functions_dict.get(command)
            if res:
                print(res(*values))
            elif res == "exit" or res == "0":
                print("выход из модуля баз данных")
                break
            else:
                print("Данная функция не поддерживается!!!")
                break


class CustomsofficersDataBase:
    def __init__(self):
        self.__db_name = "customs_officers.db"

    @property
    def db_name(self):
        return self.__db_name

    def create_db(self):
        query = """
        CREATE TABLE IF NOT EXISTS `customs_officers` (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            soname TEXT,
            rank TEXT,
            email TEXT,
            login TEXT,
            password TEXT,
            access_level TEXT);
        """
        return query

    def insert_data_into_db(self):
        query = """
        INSERT INTO 
            `customs_officers` (name, soname, rank, email, login, password, access_level) 
        VALUES (
            ?, ?, ?, ?, ?, ?, ?);
        """
        return query

    def search_user_from_db(self, data):
        query = "SELECT * FROM `customs_officers` WHERE name LIKE '%" + data + "%';"
        return query

    def refresh_data_in_db(self):
        query = """SELECT * FROM `customs_officers`;"""
        return query

    def delete_user_from_db(self):
        query = ""


# db = CustomsofficerDataBase()
# print(db.db_name)
history_path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"

with open(history_path, 'w'):
    pass