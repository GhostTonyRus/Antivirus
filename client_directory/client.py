"""
░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
"""
####################
# Modules
####################
import json
import socket
import ssl
import sys
import threading
import time
from datetime import datetime
####################
# Constants
####################
IP = "127.0.0.1"
PORT = 12345
SERVER_ADDRESS = (IP, PORT)

class Client:
    def __init__(self):
        self.__family = socket.AF_INET
        self.__connect_type = socket.SOCK_STREAM
        self.__client = socket.socket(self.__family, self.__connect_type)
        self.__key_file = "C:\\PycharmProjects\\Antivirus\\client_directory\\certificates\\privatKey.key"
        self.__certificate_file = "C:\\PycharmProjects\\Antivirus\\client_directory\\certificates\\certificate.crt"
        self.__datetime = datetime.now()
        self.__custom_datetime = self.__datetime.strftime("%Y-%m-%d %H:%M:%S")

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
        except socket.error as ex:
            print(f"Ошибка подключения: {ex}")
            # sys.exit()
            return False

    def receive_msg(self):
        """получаем сообщение от сервера"""
        while True:
            try:
                data = self.__client.recv(4096)
                if data:
                    print(f"Сообщение от сервера: {data.decode('utf-8')}")
                elif len(data) == 0:
                    print(f"Сообщение от сервера: {data.decode('utf-8')}")
                    break
            except socket.error as error:
                self.disconnect_from_server()
                break

    def send_msg(self, *args):
        """получаем данные от пользователя и отправляем их"""
        obj = {
            "data": [*args]
        }
        while True:
            time.sleep(1)
            if args == "exit":
                self.disconnect_from_server()
                break
            elif len(args) == 0:
                print("Сообщение не дол  жно быть пустым")
                continue
            elif args:
                # отправляем данные
                msg = json.dumps(obj)
                self.__client.sendall(msg.encode())

    def disconnect_from_server(self):
        """отключаемся от сервера"""
        try:
            self.__client.shutdown(socket.SHUT_RDWR)
            self.__client.close()
        except socket.error as error:
            pass

    def main(self, server_address):
        """главный метод, отвечающий за присоединение к серверу"""
        # подлкючаеся к серверу
        self.connect_to_server(server_address)
        # запуск получения сообщений
        thread_receive = threading.Thread(target=self.receive_msg)
        thread_receive.start()
        # запуск отправки сообщения
        thread_send_msg = threading.Thread(target=self.send_msg)
        thread_send_msg.start()

if __name__ == '__main__':
    client = Client()
    client.connect_to_server(SERVER_ADDRESS)
    client.send_msg("antonmakeev18@gmail.com", "12345")
    time.sleep(2)
    client.send_msg("exit")
