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
open_ports = []
PORT_MIN = 0
PORT_MAX = 65535
IP = "127.0.0.1"


class PortScanner:
    def portscan(self, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((IP, port))
            return True
        except:
            return False

    def get_ports(self, mode):
        if mode == 1:
            for port in range(1, 1024):
                queue.put(port)
        elif mode == 2:
            for port in range(1, 49152):
                queue.put(port)

    def worker(self):
        while not queue.empty():
            port = queue.get()
            if self.portscan(port):
                print(f"Порт {port} открыт")
                open_ports.append(port)
                time.sleep(1)

    def run_scanner(self, threads=100, mode=2):
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

        print("Открытые порты:", open_ports)

if __name__ == '__main__':
    # p = PortScanner()
    # p.run_scanner(100, 2)
    PortScanner().run_scanner(100, 1)
