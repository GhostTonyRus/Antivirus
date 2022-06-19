import sys
import time
import logging
import threading

import psutil as psutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.disks = psutil.disk_partitions()

    # def on_any_event(self, event):
    #     print(event.event_type, event.src_path)

    def on_created(self, event):
        print("создана", event.src_path)

    def on_deleted(self, event):
        print("удалена", event.src_path)

    def on_modified(self, event):
        print("модифицирована", event.src_path)

    def on_moved(self, event):
        print("перемещена", event.src_path)

    def main(self, disk=None):
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path="C:\\", recursive=False)
        observer.start()

        while True:
            try:
                pass
            except KeyboardInterrupt:
                observer.stop()

    def get_info(self):
        for disk in range(len(self.disks)):
            self.main(self.disks[disk].device+"\\")


if __name__ == '__main__':
    hander = MyHandler()
    thread = threading.Thread(target=hander.get_info)
    thread.start()
    thread.join()
