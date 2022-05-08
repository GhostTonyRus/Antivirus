'''
Usage: python3 usb_eject.py
OS: Window7 and later
Eject the usb storage when the usb device plugin your PC!
'''
import os
import time
from time import sleep
import subprocess
from datetime import datetime

class UsbLock:

    def __init__(self):
        self.__msg_datetime = datetime.now()
        self.__custom_msg_datetime = self.__msg_datetime.strftime('%Y-%m-%d %H:%M:%S')
        try:
            path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\locked_usb.txt"
            os.remove(path)
        except FileNotFoundError as err:
            ...

    @staticmethod
    def monitorUSBStorage():
        label = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
        'T','U','V','W','X','Y','Z']
        monitorDisk = []
        existingDisk = []
        for i in label:
            try:
                file = open(i+':/')
            except Exception as e:
                '''
                error = 2  => не найдено
                error = 13 => отказано в доступе (существует!)
                '''
                if(e.errno == 13):
                    res = f"Диск : {i} существует"
                    existingDisk.append(res)

                else:
                    monitorDisk.append(i)

        return "\n".join(existingDisk), monitorDisk

    def logging_locked_usb(self, value):
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\locked_usb.txt"
        try:
            with open(path, "a", encoding="utf-8") as file:
                file.write(f"{value} | {datetime.now().strftime('%H:%M:%S %m-%d-%Y')}\n")
        except FileExistsError as err:
            return err

    def main(self):
        existent_disks, non_existent_disks = self.monitorUSBStorage()
        print("Мониторинг.....")
        print("Проверка...")
        while(True):
            isININ = False
            disk = ''
            for i in non_existent_disks:
                try:
                    file = open(i+':/')
                except Exception as e:
                    if(e.errno == 13):
                        # print(f"Диск : {i} существует!")
                        isININ = True
                        disk = i
                        break
            if(isININ):
                tmpFile = open('tmp.ps1','w')
                tmpFile.write('$driveEject = New-Object -comObject Shell.Application\n')
                tmpFile.write('$driveEject.Namespace(17).ParseName("'+disk+':").InvokeVerb("Eject")')
                tmpFile.close()
                process = subprocess.Popen(['powershell.exe', '-ExecutionPolicy','Unrestricted','./tmp.ps1'])
                process.communicate()
                res = f"Устройство {disk} заблокировано"
                # return res
                self.logging_locked_usb(res)
                return True
            continue
            #     break

            # задержка на 2 секунды
            # time.sleep(2)

if __name__ == '__main__':
    usb = UsbLock()
    while True:
        print(usb.main())

