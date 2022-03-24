""""
ОТСЛЕЖИВАЕМ ПРОЦЕССЫ
"""

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
        self._process_property = {
            "Caption": None,
            "CreationDate": None,
            "ProcessID": None
        }

        self._process_watcher = wmi.WMI().Win32_Process.watch_for(notify_filter)

    def update(self):
        """обновляет поляЮ когда происходит событие, определённое значением notify_filter,
        """
        process = self._process_watcher()
        self._process_property["EventType"] = process.event_type
        self._process_property["Caption"] = process.Caption
        self._process_property["CreationDate"] = process.CreationDate
        self._process_property["ProcessID"] = process.ProcessID

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


class Monitor(Thread):
    def __init__(self, action):
        self._action = action
        Thread.__init__(self)

    def run(self):
        pythoncom.CoInitialize()
        process_monitor = ProcessMonitor(self._action)
        while True:
            process_monitor.update()
            print(
                date_time_format(process_monitor.creation_date),
                process_monitor.event_type,
                process_monitor.caption,
                process_monitor.process_id
            )
        pythoncom.CoUninitialize()

    def main(self):
        self.start()

if __name__ == '__main__':
    mon_creation = Monitor("creation")
    mon_creation.start()

    mon_deletion = Monitor("deletion")
    mon_deletion.start()

