"""
Файл для сбора информации о системе
"""

import os
from datetime import datetime
from uuid import getnode as get_mac # получаем MAC-адрес машины
from speedtest import Speedtest # замеряем характеристики интернета
import wmi
import platform # для сбора информации об ОС
import psutil # для работы с низкоуровнеными системными функциями

class InfoSystem:
    def __init__(self):
        # self.__speedtest = Speedtest()
        ...

    def get_system_info(self):
        # раздел с информацией о компьютере
        operating_system_discharge = platform.machine() # разряд операционной системы
        operating_system = platform.platform() # наименование операционной системе
        name_operation_system = platform.system() # название операционной системы
        computer_name = platform.node()
        user_name = os.getlogin()

        # раздел с материнской платой
        mother_board = wmi.WMI().Win32_BaseBoard()[0] # материнская плата
        bios = wmi.WMI().Win32_BIOS()[0] # биос
        motherboard_manufacturer = mother_board.Manufacturer[0:9] # производитель материнской платы
        motherboard_chipset = mother_board.Product # чипсет материнской платы
        processor_name = platform.processor() # наименование процессора
        bios_manufacturer = bios.Manufacturer # производитель BIOS
        bios_version = bios.Version # версия биос
        cpu_frequency = psutil.cpu_freq() # частота процессора
        ram = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"

        # раздел с дисплеем
        display = wmi.WMI().Win32_DisplayControllerConfiguration()[0]
        monitor = wmi.WMI().Win32_DesktopMonitor()[0]
        video_adapter = display.Caption # наименование видеокарты
        video_3d_accelerator = display.Caption # наименование 3D акселератора
        videomode = display.VideoMode.split()
        videomode[1] = "на"
        videomode[3] = "пикселей"
        videomode[-1] = "герц"
        videoMode = " ".join(videomode).replace("True", "").replace("Color", "").replace(",", "и")
        monitor_manufacturer = monitor.MonitorManufacturer
        monitor_name = monitor.Caption

        # раздел с переферией
        periphery = wmi.WMI().Win32_PointingDevice()
        info_about_periphery = ""
        for i in range(len(periphery)):
            info_about_periphery += f"""
            название устройства: {periphery[i].Description}
            ID устройства: {periphery[i].DeviceID}"""

        # раздел с сетью
        disk = wmi.WMI().Win32_LogicalDisk()
        info_about_disk = ""
        for i in range(len(disk)):
            info_about_disk += f"""
            имя диска: {disk.Caption}
            описание: {disk.Description}
            размер: {round(int(disk.Size) / (1024.0 ** 3)) if disk == None else "НЕТ ДАННЫХ"}
            файловая система: {disk.FileSystem if disk.FileSystem != None else "НЕТ ДАННЫХ"}\n"""

        # раздел с мультимедией
        sound = wmi.WMI().Win32_SoundDevice()
        info_about_sound = ""
        for i in range(len(sound)):
            info_about_sound += f"""
            производитель: {sound[i].Manufacturer}
            название устройства: {sound[i].Name}
            ID устройства: {sound[i].PNPDeviceID}\n"""

        # раздел с сетью
        network = wmi.WMI().Win32_NetworkAdapter()[0]
        network_adapter = network.AdapterType # сетевой адаптер
        network_description = network.Description # описание сети
        network_macaddress = get_mac() # mac-адрес
        network_servicename = network.ServiceName # служебное имя сети

        zone = psutil.boot_time() # время, заданное на компьютере
        time = datetime.fromtimestamp(zone) # переводим данные в читабельный вид
        info = f"""
        КОМПЬЮТЕР
        
            разряд операционной системы: {operating_system_discharge}
            операционная система: {name_operation_system}
            наименование операционной системы: {operating_system}
            имя комрьютера: {computer_name}
            имя пользователя: {user_name}
        
        МАТЕРИНСКАЯ ПЛАТА
        
            производитель материнской платы: {motherboard_manufacturer}
            чипсет материнской платы: {motherboard_chipset}
            наименование процессора: {processor_name}
            частота процессора: {cpu_frequency}
            производитель BIOS: {bios_manufacturer}
            версия BIOS: {bios_version}
            оперативная память: {ram} 
        
        ДИСПЛЕЙ
        
            видеокарта: {video_adapter}
            3D акселератор: {video_3d_accelerator}
            видеомод: {videoMode}
            производитель монитора: {monitor_manufacturer}
            монитор: {monitor_name}
        
        МУЛЬТИМЕДИЯ
            {info_about_sound}
            
        ЖЁСТКИЕ ДИСКИ
            {info_about_disk}
            
        СЕТЬ
        
            сетевой адаптер: Ethernet 802.3
            описание сети: {network_description}
            mac-адресс: {network_macaddress}
            служебное имя сети: {network_servicename}
        
        ПЕРЕФЕРИЯ
            {info_about_periphery}
     
        ВРЕМЯ
    
            системное время: {str(time)[:19]}
        """.replace("\t", "")
        return info

    def get_download_and_upload_internet_speed(self):
        download = float(str(self.__speedtest.download())[0:2] + "."
                         + str(round(self.__speedtest.download(), 2))[1]) * 0.125 # входящая скорость
        # (домножаем на 0.125 для перевода в мегабайты)
        upload = float(str(self.__speedtest.upload())[0:2] + "."
                       + str(round(self.__speedtest.download(), 2))[1]) * 0.125 # исходящая скорость
        # (домножаем на 0.125 для перевода в мегабайты)
        return download, upload

    def main(self):
        res = self.get_system_info()
        return res


if __name__ == '__main__':
    info = InfoSystem()
    print(info.main())

