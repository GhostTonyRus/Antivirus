""""
ОТСЛЕЖИВАЕМ ПРОЦЕССЫ
"""
import threading
import time
import os
from datetime import datetime
import psutil


class GetProgramActivity:
    def __init__(self):
        self.path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\program_activity.txt"
        with open(self.path, "w"):
            ...

    def run(self):
        while True:
            time.sleep(3)
            for proc in psutil.process_iter():
                with open(self.path, "a", encoding="utf-8") as file:
                    with proc.oneshot():
                        data = f"{proc.name()} - {proc.status()} - {str(psutil.cpu_percent(1))+'%'} - {str(round(proc.memory_info().rss / 1000000, 1)) + 'МБ'} - {datetime.now().strftime('%H:%M:%S %m-%d-%Y')}\n".replace("\t", "").replace("running", "запущено")
                        file.write(data)

    def main(self):
        thread = threading.Thread(target=self.run)
        thread.start()


class GetNetworkStatistics:
    def __init__(self):
        self.path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\network_activity.txt"
        with open(self.path, "w"):
            ...

    def run(self):
        connections = psutil.net_connections()
        while True:
            time.sleep(3)
            for connection in connections:
                time.sleep(2)
                with open(self.path, "a", encoding="utf-8") as file:
                    data = f"{connection} | {datetime.now().strftime('%H:%M:%S %m-%d-%Y')}\n"
                    file.write(data)

    def main(self):
        thread = threading.Thread(target=self.run)
        thread.start()



if __name__ == '__main__':
    # n = GetProgramActivity()
    # n.main()
    n = GetNetworkStatistics()
    n.main()
    # n = GetNetworkConnections()
    # n.run()