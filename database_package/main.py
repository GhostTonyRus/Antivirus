import os
from datetime import datetime
import sqlite3
from sqlite3 import Error
from logging_package import Logging

declaration_database = """
Графа 1. Декларация
Графа 2. Отправитель/Экспортер
Графа 3. Формы
Графа 4. Отгрузочные спецификации
Графа 5. Всего товаров
Графа 6. Всего мест
Графа 7. Справочный номер
Графа 8. Получатель
Графа 9. Лицо, ответственное за финансовое урегулирование
Графа 11. Торгующая страна
Графа 12. Общая таможенная стоимость
Графа 14. Декларант
Графа 15. Страна отправления
Графа 15 (a). Код страны отправления
Графа 16. Страна происхождения
Графа 17. Страна назначения
Графа 17 (a). Код страны назначения
Графа 18. Идентификация и страна регистрации транспортного средства при отправлении/прибытии
Графа 19. Контейнер
Графа 20. Условия поставки
Графа 21. Идентификация и страна регистрации активного транспортного средства на границе
Графа 22. Валюта и общая сумма по счету
Графа 23. Курс валюты
Графа 24. Характер сделки
Графа 25. Вид транспорта на границе
Графа 26. Вид транспорта внутри страны
Графа 29. Орган въезда/выезда
Графа 30. «Местонахождение товаров»
Графа 31. Грузовые места и описание товаров
Графа 32. Товар
Графа 33. Код товара
Графа 34. Код страны происхождения
Графа 35. Вес брутто (кг)
Графа 36. Преференция
Графа 37. Процедура
Графа 38. Вес нетто (кг)
Графа 39. Квота
Графа 40. Общая декларация/Предшествующий документ
Графа 41. Дополнительные единицы
Графа 42. Цена товара
Графа 43. Код МОС
Графа 44. Дополнительная информация / Предоставленные документы
Графа 45. Таможенная стоимость
Графа 46. «Статистическая стоимость»
Графа 47. Исчисление платежей
Графа 47. Исчисление платежей	Вид	Основа начисления	Ставка	Сумма	СП
Графа 48. Отсрочка платежей
Графа 54. Место и дата
графа B «Подробности подсчета»
"""


class DataBase:
    __logger = Logging("database_package")  # журнал логирования

    def __init__(self, database_name):
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.database_name = database_name
        self.__path = f"C:\\PycharmProjects\\ANTIVIRUS\\database_package\\{self.database_name}"
        self.connection = sqlite3.connect(self.__path)
        self.cursor = self.connection.cursor()
        if not self.database_name in os.listdir():
            self.__logger.register_database_actions(
                f"инициализация базы данных {self.database_name} | {self.__custom_datetime}\n")

    def get_tables_from_database(self):
        """метод для получения таблиц из базы данных"""
        try:
            with self.connection:
                self.cursor.execute("""
                        SELECT name FROM SQLITE_MASTER WHERE TYPE = "table" """)
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
                self.cursor.execute(f"""
                SELECT login, password FROM `{table_name}` WHERE login = "{login}" AND password = "{password}" 
                """)
                data = self.cursor.fetchall()
                if data:
                    for d in data:
                        users[d[0]] = d[1]
                        for user_login, user_password in users.items():
                            if user_login == login and user_password == password:
                                return True
                            else:
                                return "ВВЕДЕНЫ НЕВЕРНЫЕ ДАННЫЕ!"
        except sqlite3.Error as err:
            return err



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
            return err


class OfficerDatabase(DataBase):
    """База данных, содержащаяся в себя информацию о дложностных лицах"""

    __logger = Logging("database_package")

    def __init__(self, database_name):
        super(OfficerDatabase, self).__init__(database_name)
        self.access_levels = {
            0: "SuperUser",
            1:
                ["младший лейтенант таможенной службы",
                 "лейтенант таможенной службы",
                 "старший лейтенант таможенной службы",
                 "капитан таможенной службы"],
            2: ["майор таможенной службы",
                "подполковник таможенной службы",
                "полковник таможенной службы"],
            3: ["генерал-майор таможенной службы",
                "генерал-лейтенант таможенной службы",
                "генерал-полковник таможенной службы"]
        }

    def create_table(self, table_name):

        try:
            with self.connection:
                self.cursor.execute(
                    f"""CREATE TABLE IF NOT EXISTS {table_name} (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                soname TEXT,
                rank TEXT,
                email TEXT,
                login TEXT,
                password TEXT,
                access_level INTEGER NULL) 
                """
                )
            self.connection.commit()
            if not f"{table_name}" in self.get_tables_from_database():
                self.__logger.register_database_actions(f"создана таблица {table_name}")
        except sqlite3.Error as err:
            return err

    def insert_data_to_table(self, table_name: str, *args):
        values = args
        rank = args[2]
        self.access_level = None  # переменная, со значением ранга доступа
        for idx in range(1, 4):
            level = self.access_levels.get(idx)
            if rank in level:
                self.access_level = idx
        try:
            with self.connection:
                self.cursor.execute("""
                INSERT INTO `{table_name}` 
                    (user_id, name, soname, rank, email, login, password, access_level)
                VALUES 
                    (NULL, "{}", "{}", "{}", "{}", "{}", "{}", "{}")
                """.format(table_name=table_name, *values))
                self.connection.commit()
                self.__logger.register_database_actions(
                    f"добавление данных в таблицу {table_name}"
                )
        except sqlite3.Error as err:
            return err

    def get_data_from_table(self, table_name: str):
        """метод для получения данных из таблицы"""
        data_from_db = {}
        try:
            with self.connection:
                self.cursor.execute(f"""
                   SELECT * FROM `{table_name}`""")
                data = self.cursor.fetchall()
                self.connection.commit()
                # print("id - Имя - Фамилия - Отчетсво - email - Пароль - Подтвердите пароль")
                for d in data:
                    if d:
                        res = f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]} - {d[6]} - {d[7]}"
                        data_from_db[d[0]] = res
                    else:
                        print("Данные отсутствуют")
                self.__logger.register_database_actions(
                    f"получаем данные из таблицы {table_name}"
                )
                return "\n" + "\n".join(data_from_db.values())
        except Error as err:
            return err


class CustomsDeclarationsDataBase:
    pass


class UsersDataBase:
    __logger = Logging("database_package")  # журнал логирования

    def __init__(self, database_name):
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.database_name = database_name
        self.__path = f"C:\\PycharmProjects\\ANTIVIRUS\\database_package\\{self.database_name}"
        self.connection = sqlite3.connect(self.__path)
        self.cursor = self.connection.cursor()
        if not self.database_name in os.listdir():
            self.__logger.register_database_actions(
                f"инициализация базы данных {self.database_name} | {self.__custom_datetime}\n")

    def get_tables_from_database(self):
        """метод для получения таблиц из базы данных"""
        try:
            with self.connection:
                self.cursor.execute("""
                SELECT name FROM SQLITE_MASTER WHERE TYPE = "table" """)
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
        """метод для создания таблицы в базде данных"""
        try:
            with self.connection:
                self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS `{table_name}`(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                soname TEXT,
                name TEXT, 
                patronymic TEXT,
                email TEXT,
                password TEXT)
                """)
            self.connection.commit()
            if not "users" in self.get_tables_from_database():
                self.__logger.register_database_actions(f"создана таблица {table_name}")
        except Error as err:
            print(err)
            # logger.error(err)

    def insert_data_to_table(self, table_name: str, *args):
        """метод для добавления данных в таблицу)"""
        values = args
        try:
            with self.connection:
                # (NULL, "{soname}", "{name}", "{patronymic}", "{email}", "{password}", "{confirm_password}")""")
                self.cursor.execute("""
                INSERT INTO `{table_name}` 
                    (user_id, soname, name, patronymic, email, password) 
                VALUES 
                    (NULL, "{}", "{}", "{}", "{}", "{}")""".format(table_name=table_name, *values))
                self.connection.commit()
                self.__logger.register_database_actions(
                    f"добавление данных в таблицу {table_name}"
                )
        except Error as err:
            print(err)
            # logger.error(err)

    def get_data_from_table(self, table_name: str):
        """метод для получения данных из таблицы"""
        data_from_db = {}
        try:
            with self.connection:
                self.cursor.execute(f"""
                SELECT * FROM `{table_name}`""")
                data = self.cursor.fetchall()
                # logger.info("Данные успешно получены из базы данных")
                self.connection.commit()
                # print("id - Имя - Фамилия - Отчетсво - email - Пароль - Подтвердите пароль")
                for d in data:
                    if d:
                        res = f"{d[0]} - {d[1]} - {d[2]} - {d[3]} - {d[4]} - {d[5]} - {d[6]}"
                        # print(res)
                        data_from_db[d[0]] = res
                    else:
                        print("Данные отсутствуют")
                self.__logger.register_database_actions(
                    f"получаем данные из таблицы {table_name}"
                )
                return "\n" + "\n".join(data_from_db.values())
        except Error as err:
            ...
            # logger.error(err)

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

    def delete_date_from_table(self, table_name: str, id: int):
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
    ...
    # users_db = UsersDataBase("customs_user.db")
    # users_db.create_table("users")
    # print(users_db.get_tables_from_database())
    # users_db.get_data_from_table("users")
    # users_db.insert_data_to_table("users", "Anthony", "Tony", "Николаевич", "tonystark18@gmail.com", "Rocestear200", "Rocestear200")
    # # users_db.delete_date_from_table(1)
    # users_db.delete_database("customs_user.db")

    officers_db = OfficerDatabase("customs_officers.db")
    # officers_db.create_table("customs_officers_users")
    # print(officers_db.get_tables_from_database())
    # officers_db.insert_data_to_table("customs_officers_users",
    #     "admin",
    #     "admin",
    #     "administrator",
    #     "admin@gmail.com",
    #     "Admin",
    #     "Admin",
    #     0
    # )
    # print(officers_db.get_data_from_table("customs_officers_users"))
    print(officers_db.check_data("customs_officers_users", "Admin", "Admin"))
