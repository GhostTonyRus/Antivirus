"""
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
####################
# Modules
####################
import json
import pickle
import socket
import ssl
import threading
import os
from datetime import datetime
from database_package import UsersDataBase
from logging_package import Logging
from antivirus_package import Two_factor_authentication
####################
# Constants
####################
IP = "127.0.0.1"
PORT = 12345
SERVER_ADDRESS = (IP, PORT)
MANUAL = """
+---+--------------------------------------------------+
| 1 | посмотреть таблицы в базе данных                 |
+---+--------------------------------------------------+
| 2 | получить данные из таблицы                       |
|   | (введите название таблицы)                       |
+---+--------------------------------------------------+
| 3 | добавить данные в таблицу                        |
|   | (введите название таблицы и данные через пробел) |
+------------------------------------------------------+
| 4 | изменить данные в таблице                        |
|   | (id поля и значение через пробел)                |
+------------------------------------------------------+
"""

def register_server_action(value):
    path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\register_server_action.txt"
    while True:
        try:
            with open(path, "a", encoding="utf-8") as file:
                file.write(value)
        except FileExistsError as err:
            return err

two_factor_authentication = Two_factor_authentication()

class Server:
    def __init__(self, key_file=None, certificate_file=None):
        self.__action_log = Logging("server_package")
        self.__family = socket.AF_INET
        self.__type = socket.SOCK_STREAM
        self.__server = socket.socket(self.__family, self.__type)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # временно
        # self.__key_file = key_file
        self.__key_file = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\certificates\\privatKey.key"
        self.__certificate_file = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\certificates\\certificate.crt"
        ########
        self.__clients = []
        self.__msg_datetime = datetime.now()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.__user_db = UsersDataBase()

        self.server_commands = {
            "1" :"посмотреть таблицы в базе данных",
            "2" :"получить данные из таблицы",
            "3" :"добавить данные в таблицу",
            "4" :"изменить данные в таблице"
        }
        temporary_path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\temporary_actions.txt"
        with open(temporary_path, 'w'):
            pass

    def temporary_actions(self, value, time):
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\temporary_actions.txt"
        try:
            with open(path, "a", encoding="utf-8") as file:
                file.write(f"{value} | {time}\n")
        except FileExistsError as err:
            return err

    def thread_db_connection(self, func, table_name):
        thread = threading.Thread(target=func, args=(table_name,))
        thread.start()
        return thread

    def start_client_thread(self, func, connection, client_address):
        """присоединение пользователей к серверу и
        добавляем каждого пользователя в отдельный поток"""
        notification = f"Пользователь {client_address} присоединился к серверу\n"
        print(notification)
        thread = threading.Thread(target=func, args=(connection, client_address,))
        thread.start()
        return thread

    def ssl_wrap_connection(self, server):
        """подключаем ssl соединение"""
        ssl_connection = ssl.wrap_socket(server, server_side=True,
                                         keyfile=self.__key_file, certfile=self.__certificate_file)
        return ssl_connection

    def bind_server(self, server_address):
        """бинд сервера"""
        self.__server = self.ssl_wrap_connection(self.__server)
        self.__server.bind(server_address)
        print("Подлючение к ip {} port {}".format(*server_address))
        self.__action_log.register_server_actions(
            "Сервер подключён по адресу ip {} port {}".format(*server_address))
        self.temporary_actions("Сервер подключён по адресу ip {} port {}".format(*server_address),
                               datetime.now().strftime("%H:%M:%S %m-%d-%Y"))

    def start_server(self, num_of_users):
        """запуск сервера"""
        self.__server.listen(int(num_of_users))
        self.__server.setblocking(False)
        print("Ожидание подлкючения пользователей: ")
        self.__action_log.register_server_actions(f"Ожидание подключение пользователей")
        self.temporary_actions(f"Ожидание подключение пользователей", datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
        while True:
            # принимаем подключение и адрес подключившихся пользователей
            self.__server.setblocking(True)
            self.connection, self.client_addr = self.__server.accept()
            self.__clients.append(self.connection)
            self.__action_log.register_server_actions(
                f"Пользователь {self.client_addr} подключился к серверу")
            self.temporary_actions(f"Пользователь {self.client_addr} подключился к серверу",
                                   datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
            # добавление пользователей в поток
            self.start_client_thread(func=self.get_users_connection_and_messages, connection=self.connection,
                                     client_address=self.client_addr)
            continue

    # генерируем код для отправки
    def generate_code(self):
        code = two_factor_authentication.generate_code()
        return code

    # отправляем письмо с кодом
    def send_email_code(self, email, code):
        two_factor_authentication.send_email(email=email, msg=code)
        print("сообщение отправлено")

    # получаем соединения от пользователя и сообщения
    def get_users_connection_and_messages(self, connection, client_address):
        user_db = UsersDataBase("customs_user")
        """ожидаем подключения от пользователей"""
        all_data = bytearray()
        while True:
            # получаем тип подключения из словаря
            try:
                # получаем данные от пользователя
                self.__server.setblocking(True)
                data = connection.recv(4096)
                if data == "exit":
                    print(f"Пользователь {client_address} отключился от сервера 150 строка")
                    self.__action_log.register_server_actions(
                        f"Пользователь {client_address} отключился от сервера")
                    self.temporary_actions(f"Пользователь {client_address} отключился от сервера",
                                           datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
                    self.close_connection(connection)
                    break
                # если нет данных
                if not data:
                    print(f"Сообщение от пользователя отсутствуют: {client_address}")
                    self.__action_log.register_server_actions(
                        f"Сообщение от пользователя отсутствуют: {client_address}")
                    self.temporary_actions(f"Сообщение от пользователя отсутствуют: {client_address}",
                                           datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
                    self.close_connection(connection)
                    break
                if data:
                    self.__action_log.register_server_actions(
                        f"Пользователь {self.client_addr} прислал сообщение: {data.decode('utf-8')}")
                    self.temporary_actions(f"Пользователь {self.client_addr}: прислал сообщение {data.decode('utf-8')}",
                                           datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
                    all_data += data
                    obj = json.loads(all_data)
                    res = self.__user_db.get_data_from_table(obj) # получаем данные из базы данных
                    if res:
                        self.send_message(connection, "True")
                        self.send_email_code(email="antonmakeev18@gmail.com", code=self.generate_code())
                    elif res == False:
                        self.send_message(connection, "False")
            except socket.error as error:
                self.close_connection(connection)
                break

    def send_message(self, connection, data):
        """отправляем полученное сообщение обратно клиенту"""
        connection.sendall(data.encode("utf-8"))

    def return_info_about_connections(self):
        return self.__clients

    def block_connections(self):
        ...

    # def get_email_password_from_client(self, data):
    #     for login, password in data.items():
    #         self.__user_db.get_data_from_table(login, password)

    def close_connection(self, client_connection):
        """закрываем соединение с клиентом"""
        self.__clients.remove(client_connection)
        client_connection.shutdown(socket.SHUT_RDWR)
        client_connection.close()
        print(f"Пользователь {client_connection} отключился строка")
        self.__action_log.register_server_actions(
            f"Пользователь {client_connection} отключился")
        self.temporary_actions(f"Пользователь {client_connection} отключился",
                               datetime.now().strftime("%H:%M:%S %m-%d-%Y"))

    def stop_server(self):
        try:
            self.__server.shutdown(socket.SHUT_RDWR)
        except Exception as err:
            return err
        finally:
            self.__server.close()
            self.__action_log.register_server_actions(
                "Сервер отключён")
            self.temporary_actions("Сервер отключён",
                                   datetime.now().strftime("%H:%M:%S %m-%d-%Y"))

    def main(self, server_address=("127.0.0.1", 12345), number_of_clients=10):
        """главный метод, отвечающий за запуск и бинд сервера"""
        self.bind_server(server_address)
        self.start_server(number_of_clients)
        # register_server_action("Сервер готов к работе")

if __name__ == '__main__':
    server = Server()
    server.main()
