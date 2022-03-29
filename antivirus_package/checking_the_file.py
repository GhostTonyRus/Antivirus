import json
import requests


class SaveDataJson:
    """класс предназначенный для записи и получения информации о файле,
    который был загружен для проверки"""

    @staticmethod
    def dump_json(data):
        """запись в файл"""
        with open("data.txt", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_json():
        """вывод данных из файла"""
        with open("data.txt", "r") as outfile:
            data = json.load(outfile)
            print(f"id - {data['scan_id']}")
            print(f"дата и время - {data['scan_date']}")
            print(f"всего проверок - {data['total']}")
            print(f"обнаружено вирусов - {data['positives']}")

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
        files = {"file": (self.path)}
        response = requests.post(self.url, files=files, params=self.params)
        res = response.json()
        return res["scan_id"]

    def get_info_about_file(self):
        """получаем информацию о файле"""
        resource = self.upload_file()
        self.params["resource"] = str(resource)
        report_response = requests.get(self.report_url, params=self.params)
        return report_response.json()

    def main(self):
        result = self.get_info_about_file()
        return result

if __name__ == '__main__':
    ...
    test = CheckFile("C:\\PycharmProjects\\Antivirus\\README.md")
    data = test.main()
    print(data)
    # test2 = SaveDataJson.dump_json(data)
    # test2.load_json()
    # test2 = SaveDataJson.load_json()