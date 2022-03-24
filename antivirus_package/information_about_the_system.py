"""
Файл для сбора информации о системе
"""


from datetime import datetime
from uuid import getnode as get_mac # получаем MAC-адрес машины
from speedtest import Speedtest # замеряем характеристики интернета
import platform # для сбора информации об ОС
import psutil # для работы с низкоуровнеными системными функциями

class InfoSystem:
    def __init__(self):
        self.__speedtest = Speedtest()

    def get_system_info(self):
        operating_system_discharge = platform.machine() # разряд операционной системы
        operating_system = platform.platform() # наименование операционной системе
        platform_name = platform.uname() # информаци о операционной системе
        name_operation_system = platform.system() # название операционной системы
        processor_name = platform.processor() # наименование процессора
        cpu_frequency = psutil.cpu_freq() # частота процессора
        MAC_address = get_mac()
        return operating_system_discharge, operating_system, platform_name, name_operation_system, processor_name, cpu_frequency, MAC_address

    def get_time_zone_and_time(self):
        zone = psutil.boot_time() # время, заданное на компьютере
        time = datetime.fromtimestamp(zone) # переводим данные в читабельный вид
        return str(time)[:19]

    def get_download_and_upload_internet_speed(self):
        download = float(str(self.__speedtest.download())[0:2] + "."
                         + str(round(self.__speedtest.download(), 2))[1]) * 0.125 # входящая скорость
        # (домножаем на 0.125 для перевода в мегабайты)
        upload = float(str(self.__speedtest.upload())[0:2] + "."
                       + str(round(self.__speedtest.download(), 2))[1]) * 0.125 # исходящая скорость
        # (домножаем на 0.125 для перевода в мегабайты)
        return download, upload

    def main(self):
        self.get_system_info()
        self.get_time_zone_and_time()
        self.get_download_and_upload_internet_speed()

if __name__ == '__main__':

    info = InfoSystem()
    info.main()