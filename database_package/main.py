from database_package.base_database_model import DataBaseClass
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

class CustomsDeclarationsDataBase:
    pass


class UsersDataBase:
    __logger = Logging("database_package")  # журнал логирования

    def __init__(self, database_name=None):
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.database_name = database_name
        self.__path = f"../dependencies/database_dir/customs_users.db"
        self.connection = sqlite3.connect(self.__path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name=None):
        """метод для создания таблицы в базде данных"""
        try:
            with self.connection:
                self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS `customs_users` (
                     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     Имя TEXT,
                     Фамилия TEXT,
                     Отчество TEXT,
                     email TEXT,
                     пароль TEXT);""")
            self.connection.commit()
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

    def get_data_from_table(self, data):

        """метод для получения данных из таблицы"""
        data_from_db = {}
        try:
            with self.connection:
                self.cursor.execute(f"""
                SELECT * FROM `customs_users`""")
                data_form_db = self.cursor.fetchall()
                self.connection.commit()
                for item in data_form_db:
                    data_from_db[item[-2]] = item[-1]
                # return "\n" + "\n".join(data_from_db.values())
        except Error as err:
           ...
        for email, password in data.items():
            for email_from_db, password_from_db in data_from_db.items():
                if email_from_db == email and password_from_db == password:
                    return True
                else:
                    return False
            # logger.error(err)
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
    # users = UsersDataBase()
    # print(users.get_data_from_table("antonmakeev18@gmail.com", "12345"))
    path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"

