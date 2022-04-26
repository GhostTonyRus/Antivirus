"""
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ <
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\

"""
import threading
import time

import pyfiglet
import socket
from queue import Queue
from progress.bar import IncrementalBar

queue = Queue()
PORT_MIN = 0
PORT_MAX = 65535
IP = "127.0.0.1"


class PortScanner:

    def __init__(self):
        self.open_ports = []
        self.closed_ports = []

    def portscan(self, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((IP, port))
            return True
        except:
            return False

    def get_ports(self, mode):
        variants = {
            "ПРОВЕРИТЬ ПОРТЫ В ДИАПАЗОНЕ ОТ 1 ДО 1024": 1,
            "ПРОВЕРИТЬ ПОРТЫ В ДИАПАЗОНЕ ОТ 1 ДО 49152": 2,
            "ПРОВЕРИТЬ ЗАРЕЗЕРВИРОВАННЫЕ СИСТЕМОЙ ПОРТЫ": 3,
        }
        if variants.get("ПРОВЕРИТЬ ПОРТЫ В ДИАПАЗОНЕ ОТ 1 ДО 1024"):
            for port in range(1, 1024):
                queue.put(port)
        elif mode == 2:
            for port in range(1, 49152):
                queue.put(port)
        elif mode == 3:
            ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
            for port in ports:
                queue.put(port)

    def worker(self):
        while not queue.empty():
            port = queue.get()
            if self.portscan(port):
                print(f"Порт {port} открыт")
                self.open_ports.append(str(port))
                time.sleep(1)
            else:
                self.closed_ports.append(str(port))
                time.sleep(1)

    def run_scanner(self, threads, mode):
        print("Запуск сканера порт")
        self.get_ports(mode)

        thread_list = []

        for t in range(threads):
            thread = threading.Thread(target=self.worker)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

    def main(self, value):
        self.run_scanner(100, value)
        info_about_ports = """\nОткрытыте порты:\n"""
        for port in self.open_ports:
            info_about_ports += f"""{port}\n"""
        info_about_ports += "\nЗакрыты порты:\n"
        for port in self.closed_ports:
            info_about_ports += f"""{port}\n"""
        return info_about_ports

if __name__ == '__main__':
    print(PortScanner().main(1))
