""""
ОТСЛЕЖИВАЕМ ПРОЦЕССЫ
"""
import time

import os
import wmi
from threading import Thread
import pythoncom


notify_filter_creation = "creation"
notify_filter_operation = "operation"
notify_filter_deletion = "deletion"
notify_filter_modification = "modification"

def date_time_format(date_time):
    year = date_time[:4]
    month = date_time[4:6]
    day = date_time[6:8]
    hour = date_time[8:10]
    minutes = date_time[10:12]
    seconds = date_time[12:14]
    return f"{day}/{month}/{year} {hour}:{minutes}:{seconds}"

class ProcessMonitor:
    def __init__(self, notify_filter="operation"):
        """
        при инициализации класса создаётся писок свойств процесса в виде слвоаря и определяется объект наблюдателя
        """
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\activity_registration.txt"
        with open(path, "w") as file:
            ...

        self._process_property = {
            "Caption": None,
            "CreationDate": None,
            "ProcessID": None,
            "MaximumWorkingSetSize": None,
            "Description": None,
            "OtherOperationCount": None,
        }

        self._process_watcher = wmi.WMI().Win32_Process.watch_for(notify_filter)

    def update(self):
        """обновляет поля, когда происходит событие, определённое значением notify_filter,
        """
        try:
            process = self._process_watcher()
            self._process_property["EventType"] = process.event_type
            self._process_property["Caption"] = process.Caption
            self._process_property["CreationDate"] = process.CreationDate
            self._process_property["ProcessID"] = process.ProcessID
            self._process_property["MaximumWorkingSetSize"] = process.MaximumWorkingSetSize
            self._process_property["OtherOperationCount"] = process.OtherOperationCount
        except Exception:
            ...

    # методы возвращают значения соответствующих полей списка свойств процесса
    @property
    def event_type(self):
        return self._process_property["EventType"]

    @property
    def caption(self):
        return self._process_property["Caption"]

    @property
    def creation_date(self):
        return self._process_property["CreationDate"]

    @property
    def process_id(self):
        return self._process_property["ProcessID"]

    @property
    def maximumWorkingSetSize(self):
        return self._process_property["MaximumWorkingSetSize"]

    @property
    def otherOperationCount(self):
        return self._process_property["OtherOperationCount"]

class Monitor(Thread):
    def __init__(self, action):
        self._action = action
        Thread.__init__(self)

    def run(self):
        pythoncom.CoInitialize()
        process_monitor = ProcessMonitor(self._action)
        while True:
            time.sleep(3)
            process_monitor.update()
            with open("C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\activity_registration.txt",
                      "a", encoding="utf-8") as file:
                data = (
                    date_time_format(process_monitor.creation_date) + "\t",
                    str(process_monitor.event_type) + "\t",
                    str(process_monitor.caption) + "\t",
                    str(process_monitor.process_id) + "\t",
                    str(process_monitor.maximumWorkingSetSize) + "МБ\t\t",
                    str(process_monitor.otherOperationCount) + "%",
                )
                file.write(str(" ".join(data))+"\n")

    def main(self):
        self.start()


if __name__ == '__main__':
    mon_creation = Monitor("creation")
    mon_creation.start()

    mon_deletion = Monitor("deletion")
    mon_deletion.start()

    mon_modification = Monitor("modification")
    mon_modification.start()

    mon_operation = Monitor("operation")
    mon_operation.start()
