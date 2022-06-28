import threading
import time

from client_logger import Client_logger
import psutil as psutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.__action_log = Client_logger("os_actions")

    def on_created(self, event):
        self.__action_log.register_os_system_action("создана", event.src_path)

    def on_deleted(self, event):
        self.__action_log.register_os_system_action("удалена", event.src_path)

    def on_modified(self, event):
        self.__action_log.register_os_system_action("модифицирована", event.src_path)

    def on_moved(self, event):
        self.__action_log.register_os_system_action("перемещена", event.src_path)


class SystemWatch:
    def __init__(self):
        self.disks = psutil.disk_partitions()

    def get_event(self, disk):
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path=disk, recursive=False)
        observer.start()
        while True:
            time.sleep(1)
            try:
                pass
            except KeyboardInterrupt:
                observer.stop()

    def main(self):
        for disk in range(len(self.disks)):
            thread = threading.Thread(target=self.get_event, args=(self.disks[disk].device+"\\",))
            thread.start()

if __name__ == '__main__':
    handler = SystemWatch()
    handler.main()
