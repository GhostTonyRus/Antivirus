import json
import os
import socket
import ssl
import sys
import threading
import time
from datetime import datetime

IP = "127.0.0.1"
PORT = 12345
SERVER_ADDRESS = (IP, PORT)

# класс клиент
class Client:
    """
    Файл с кодом для присоединения к серверу. Клиент отправляет сообщение и получает его обратно от сервера.
    """
    def __init__(self):
        self.__family = socket.AF_INET
        self.__connect_type = socket.SOCK_STREAM
        self.__client = socket.socket(self.__family, self.__connect_type)
        self.__key_file = "C:\\PycharmProjects\\Antivirus\\client_directory\\certificates\\privatKey.key"
        self.__certificate_file = "C:\\PycharmProjects\\Antivirus\\client_directory\\certificates\\certificate.crt"
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime("%Y-%m-%d %H:%M:%S")
        history_path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"

        with open(history_path, 'w'):
            pass

    def ssl_wrap_connection(self, client):
        """подключаем ssl соединение"""
        ssl_connection = ssl.wrap_socket(client, keyfile=self.__key_file, certfile=self.__certificate_file)
        return ssl_connection

    def connect_to_server(self, server_address):
        """подлкючение к серверу"""
        try:
            self.__client = self.ssl_wrap_connection(self.__client)
            self.__client.connect(server_address)
            print("Выполнено подлюкчение к серверу")
            return True
        except socket.error as ex:
            print(f"Ошибка подключения: {ex}")
            sys.exit()

    # отправляем сообщения на сервер
    def send_user_data(self, login, password):
        time.sleep(1)
        if len(login) == 0 or len(password) == 0:
            pass
        else:
            obj = {
                login: password,
            }
            try:
                # отправляем данные
                message = json.dumps(obj)
                self.__client.sendall(str(f"{message}").encode())
            except socket.error:
                pass

    # получаем сообщение от сервера
    def receive_msg(self):
        time.sleep(3)
        path = "C:\\PycharmProjects\\Antivirus\\client_directory\\history.txt"
        while True:
            try:
                data = self.__client.recv(4096).decode("utf-8")
                if data:
                    print(data, "from client")
                    with open(path, "w", encoding="utf-8") as file:
                        file.write(f"{data}\n")
                elif len(data) == 0:
                    self.disconnect_from_server()
                    break
            except socket.error:
                self.disconnect_from_server()
                break

    # отсоединение от сервера
    def disconnect_from_server(self):
        """отключаемся от сервера"""
        try:
            self.__client.shutdown(socket.SHUT_RDWR)
            self.__client.close()
        except socket.error as error:
            pass
        finally:
            time.sleep(1)
            self.__client.close()

    def main(self, server_address):
        """главный метод, отвечающий за присоединение к серверу"""
        # подлкючаеся к серверу
        self.connect_to_server(server_address)
        # запуск получения сообщений
        thread_receive = threading.Thread(target=self.receive_msg)
        thread_receive.start()
        # запуск отправки сообщения
        thread_send_msg = threading.Thread(target=self.send_user_data)
        thread_send_msg.start()
