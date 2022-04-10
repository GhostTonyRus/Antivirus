import json
import time

import requests

class CheckFile:
    """Класс предназначенный для проверки файла.
    Для проверки используется VirusTotal Api.
    Файл загружается при попомощи post запроса.
    Для того, чтобы получить информацию о файле используется метод get"""
    def __init__(self, path):
        self.path = path
        self.url = "https://www.virustotal.com/vtapi/v2/file/scan" # url для загрузки файла
        self.params = {"apikey": "e78d30c3bbbed09731a783a97b1a1e34f52008c8ccf61a0f161558cfe0da836b"}
        self.report_url = "https://www.virustotal.com/vtapi/v2/file/report" # url для получения информации

    def upload_file(self):
        """загружаем файл"""
        params = dict(apikey='e78d30c3bbbed09731a783a97b1a1e34f52008c8ccf61a0f161558cfe0da836b')
        with open(self.path, 'rb') as file:
            files = dict(file=(self.path, file))
            response = requests.post(self.url, files=files, params=params)
        if response.status_code == 200:
            result = response.json()
            # print(json.dumps(result, sort_keys=False, indent=4))
            return result["resource"]

    def get_info_about_file(self):
        """получаем информацию о файле"""
        resource = self.upload_file()
        params = dict(apikey='e78d30c3bbbed09731a783a97b1a1e34f52008c8ccf61a0f161558cfe0da836b',
                      resource=resource)
        response = requests.get(self.report_url, params=params)
        if response.status_code == 200:
            result = response.json()
            # print(json.dumps(result, sort_keys=False, indent=4))
            json_res = json.dumps(result, sort_keys=False, indent=4)
            # return json_res
            report = f"""
            id - {result['scan_id']}
            дата и время - {result['scan_date']}
            всего проверок - {result['total']}
            обнаружено вирусов - {result['positives']}"""
            return report

    def main(self):
        result = self.get_info_about_file()
        return result

if __name__ == '__main__':
    test = CheckFile("C:\\PycharmProjects\\Antivirus\\antivirus_package\\hosts.txt")
    data = test.main()
    print(data)





