import json
import os
import threading
import time
import queue
import requests
import asyncio
from datetime import datetime


class CheckFile:
    """Класс предназначенный для проверки файла.
    Для проверки используется VirusTotal Api.
    Файл загружается при попомощи post запроса.
    Для того, чтобы получить информацию о файле используется метод get"""

    def __init__(self):
        self.url = "https://www.virustotal.com/vtapi/v2/file/scan"  # url для загрузки файла
        self.params = {"apikey": "e78d30c3bbbed09731a783a97b1a1e34f52008c8ccf61a0f161558cfe0da836b"}
        self.report_url = "https://www.virustotal.com/vtapi/v2/file/report"  # url для получения информации
        self.antivirus_path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\"
        self.server_path = "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\"
        self.database_path = "C:\\PycharmProjects\\Antivirus\\dependencies\\database_dir\\"
        self.log_path = "C:\\PycharmProjects\\Antivirus\\dependencies\\log_dir\\"
        self.report_dir = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\report.txt"
        self.files_queue = queue.Queue()
        self.res_of_scan = []

        with open(self.report_dir, "w") as file:
            ...

    def get_files_from_dirs(self):
        for dirpath, dirnames, filenames in os.walk(self.antivirus_path):
            for file in filenames:
                self.files_queue.put(self.antivirus_path+file)

        for dirpath, dirnames, filenames in os.walk(self.server_path):
            for file in filenames:
                self.files_queue.put(self.server_path+file)

        for dirpath, dirnames, filenames in os.walk(self.database_path):
            for file in filenames:
                self.files_queue.put(self.database_path+file)

        for dirpath, dirnames, filenames in os.walk(self.log_path):
            for file in filenames:
                self.files_queue.put(self.log_path+file)

    def upload_file(self, file_from_queue):
        """загружаем файл"""
        params = dict(apikey='e78d30c3bbbed09731a783a97b1a1e34f52008c8ccf61a0f161558cfe0da836b')

        with open(file_from_queue, 'rb') as file:
            files = dict(file=(file_from_queue, file))
            response = requests.post(self.url, files=files, params=params)
            time.sleep(158)
        if response.status_code == 200:
            result = response.json()
            return result["resource"]

    def get_info_about_file(self, file_path):
        """получаем информацию о файле"""
        resource = self.upload_file(file_path)
        params = dict(apikey='e78d30c3bbbed09731a783a97b1a1e34f52008c8ccf61a0f161558cfe0da836b',
                      resource=resource)
        response = requests.get(self.report_url, params=params)
        time.sleep(150)
        if response.status_code == 200:
            result = response.json()
            json_res = json.dumps(result, sort_keys=False, indent=4)
            report = f"""
            Результат проверки:
            id - {result['scan_id']}
            время и дата - {datetime.now().strftime('%H:%M:%S %m-%d-%Y')}
            всего проверок - {result['total']}
            обнаружено вирусов - {result['positives']}\n""".replace("\t", "")
            self.res_of_scan.append(report)

    def run(self):
        files = [
            "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\activity_registration.txt",
            "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\hosts.txt",
            "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\locked_connections.txt",
            "C:\\PycharmProjects\\Antivirus\\dependencies\\log_dir\\логирование баз данных.txt",
            "C:\\PycharmProjects\\Antivirus\\dependencies\\log_dir\\логирование сервера.txt",
            "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\locked_connections.txt",
            "C:\\PycharmProjects\\Antivirus\\dependencies\\server_dir\\temporary_actions.txt",
        ]

        for file in files:
            thread = threading.Thread(target=self.get_info_about_file, args=(file,))
            thread.start()
            thread.join()


    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        thread.join()

    def main(self):
        self.start()
        return " ".join(self.res_of_scan)

if __name__ == '__main__':
    test = CheckFile()
    print(test.main())



