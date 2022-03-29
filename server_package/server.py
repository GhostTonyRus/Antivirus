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
import socket
import ssl
import threading
import os
from datetime import datetime
from database_package import UsersDataBase
from logging_package import Logging
####################
# Constants
####################
IP = "127.0.0.1"
PORT = 12345
SERVER_ADDRESS = (IP, PORT)
MANUAL = """
+---+----------------------------------+
| 1 | посмотреть таблицы в базе данных |
+---+----------------------------------+
| 2 | получить данные из таблицы       |
+---+----------------------------------+
| 3 | добавить данные в таблицу        |
+--------------------------------------+
| 4 | изменить данные в таблице        |
+--------------------------------------+

Для просмотра таблицы ввести цифру "1";
Для получения данных из таблицы ввести цифру "2" и название таблицы;
Для добавления данных в таблицу ввести цифру "3" название таблицы и данные через пробел
Для измения данных в таблице ввести  цифру "4" id поля и значение через пробел
"""

class Server:
    def __init__(self, key_file=None, certificate_file=None):
        self.__action_log = Logging("server_package")
        self.__family = socket.AF_INET
        self.__type = socket.SOCK_STREAM
        self.__server = socket.socket(self.__family, self.__type)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # временно
        # self.__key_file = key_file
        self.__key_file = "certificates/privatKey.key"
        self.__certificate_file = "certificates/certificate.crt"
        ########
        self.__clients = []
        self.__msg_datetime = datetime.now()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%Y-%m-%d %H:%M:%S')
        __file = "customs_user"
        try:
            self.__user_db = UsersDataBase(__file)
        except Exception as err:
            print(err)
        self.server_commands = {
            "1" :"посмотреть таблицы в базе данных",
            "2" :"получить данные из таблицы",
            "3" :"добавить данные в таблицу",
            "4" :"изменить данные в таблице"
        }

    def thread_stop_server(self):
        msg = input("Введите 'stop' для остановки работы сереера:\n>>>")
        print(msg)
        if msg == "stop":
            thhread = threading.Thread(target=self.stop_server)
            thhread.start()
            thhread.join()

    def thread_db_connection(self, func, table_name):
        thread = threading.Thread(target=func, args=(table_name,))
        thread.start()
        return thread

    def start_client_thread(self, func, connection, client_address):
        """присоединение пользователей к серверу и
        добавляем каждого пользователя в отдельный поток"""
        notification = f"Пользователь {client_address} присоединился к серверу"
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
            "Сервер подключён по адресу ip {} port {} | {}\n".format(*server_address, self.__custom_msg_datetime))

    def start_server(self, num_of_users):
        """запуск сервера"""
        self.__server.listen(int(num_of_users))
        self.__server.setblocking(False)
        print("Ожидание подлкючения пользователей: ")
        self.__action_log.register_server_actions(f"Ожидание подключение пользователей")
        while True:
            # принимаем подключение и адрес подключившихся пользователей
            self.__server.setblocking(True)
            self.connection, self.client_addr = self.__server.accept()
            self.__clients.append(self.connection)
            self.connection.send(f"Вы присоединились к серверу.\n"
                                 f"Ввведите номер комманды для взаимодействия с Базой Данной {MANUAL}".encode("utf-8"))
            self.__action_log.register_server_actions(
                f"Пользователь {self.client_addr} подключился к серверу")
            # добавление пользователей в поток
            self.start_client_thread(func=self.get_users_connection_and_messages, connection=self.connection,
                                     client_address=self.client_addr)
            continue

    def get_users_connection_and_messages(self, connection, client_address):
        user_db = UsersDataBase("customs_user.db")
        """ожидаем подключения от пользователей"""
        while True:
            # получаем тип подключения из словаря
            try:
                # получаем данные от пользователя
                self.__server.setblocking(True)
                data = connection.recv(4096)
                if data == "exit":
                    print(f"Пользователь {client_address} отключился от сервера")
                    self.__action_log.register_server_actions(
                        f"Пользователь {client_address} отключился от сервера")
                    self.close_connection(connection)
                    break
                try:
                    data = data.decode("utf-8").split()
                    number_command = data[0]
                except IndexError:
                    self.__action_log.register_server_actions(
                        f"Сообщение от пользователя: {client_address}: 'exit'")
                    self.close_connection(connection)
                # если нет данных
                if not data:
                    print(f"Сообщение от пользователя отсутствуют: {client_address}")
                    self.__action_log.register_server_actions(
                        f"Сообщение от пользователя отсутствуют: {client_address}")
                    self.close_connection(connection)
                    break
                if data[0] in self.server_commands.keys():
                    print(f"Сообщение от пользователя {client_address}: {data}")
                    self.__action_log.register_server_actions(
                        f"Сообщение от пользователя {client_address}: {data}")
                    if number_command == "1":
                        connection.sendall(user_db.get_tables_from_database().encode("utf-8"))
                    elif number_command == "2":
                        connection.sendall(user_db.get_data_from_table("users").encode("utf-8"))
                    elif number_command == "3":
                        table_name = data[1]
                        values = data[2:]
                        try:
                            user_db.insert_data_to_table(table_name, values)
                            ...
                        except Exception as err:
                            self.close_connection(connection)
                        connection.sendall(f"Данные успешно добавлены! {data[1]}".encode("utf-8"))
                    elif number_command == "4":
                        table_name = data[1]
                        id = data[2]
                        row = data[3]
                        value = data[4]
                        try:
                            user_db.update_data_in_table(table_name, id, row, value)
                        except Exception as err:
                            self.close_connection(connection)
                        connection.sendall("Данные успешно обновлены!".encode("utf-8"))

            except socket.error as error:
                self.close_connection(connection)
                break

    def send_message(self, connection, data):
        """отправляем полученное сообщение обратно клиенту"""
        connection.sendall(data.encode("utf-8"))

    def close_connection(self, client_connection):
        """закрываем соединение с клиентом"""
        self.__clients.remove(client_connection)
        client_connection.shutdown(socket.SHUT_RDWR)
        client_connection.close()
        print(f"Пользователь {client_connection} отключился")
        self.__action_log.register_server_actions(
            f"Пользователь {client_connection} отключился")

    def stop_server(self):
        try:
            self.__server.shutdown(socket.SHUT_RDWR)
        except Exception as err:
            return err
        finally:
            self.__server.close()

    def main(self, server_address, number_of_clients):
        """главный метод, отвечающий за запуск и бинд сервера"""
        manual = """
        +--------------------------------+
        | 1 | для запуска сервера        |
        +--------------------------------+
        | exit/0 | выход из меню сервера |
        +--------------------------------+
        """
        print(manual)
        while True:
            response = str(input("\n>>> "))
            if response == "1":
                self.bind_server(server_address)
                self.start_server(number_of_clients)
            elif response == "exit" or response == "0":
                print("выход из меню сервера")
                break
            else:
                print("Такой команды нет!")
                continue

if __name__ == '__main__':
    server = Server()
    server.main(SERVER_ADDRESS, 10)

