import gc
import hashlib
import json
import os
import threading
import time
from datetime import datetime
import psutil
import uuid

class DisksFromOs:
    def __init__(self):
        self.name_disks = psutil.disk_partitions()
        self.__disks = []

    def get_disks(self):
        for disk in self.name_disks:
            self.__disks.append(disk[0])

    @property
    def disks(self):
        self.get_disks()
        return self.__disks


class AntivirusEngine:

    def __init__(self):
        self.res_of_scan =  []
        self.virus_file_md5 = []
        self.virus_file_sha256 = []
        self.virus_file_sha1 = []


    def get_files_from_dirs(self):
        files_from_dirs = []
        try:
            for dirpath, dirnames, filenames in os.walk("C:\\"):
                for file in filenames:
                    res = os.path.join(dirpath, file)
                    last_change_file = str(str(time.ctime(os.stat(res).st_mtime)))
                    if last_change_file.endswith("2022") and "Jun" in last_change_file:
                        files_from_dirs.append(res)
        except FileNotFoundError:
            ...
        except PermissionError:
            ...
        except OSError:
            ...
        return files_from_dirs

    #############################################
    #                   MD5                     #
    #############################################
    def get_md5_hashes(self):
        md5_hashes = []
        files = self.get_files_from_dirs()
        for file in files:
            try:
                with open(file, "rb") as file:
                    bytes = file.read()
                    md5_hash = hashlib.md5(bytes).hexdigest()
                    md5_hashes.append(md5_hash)
            except FileNotFoundError:
                ...
            except PermissionError:
                ...
            except OSError:
                ...
        return md5_hashes

    def md5_hash_checker(self):
        path = "C:\\PycharmProjects\\Antivirus\\dependencies\\antivirus_dir\\signatures\\MD5 Virus Hashes.txt"
        file_hashes = self.get_md5_hashes()
        virus_file = []
        with open(path, "r") as file:
            hashes = file.read().split()
            for hash in hashes:
                for item in file_hashes:
                    if hash == item:
                        self.virus_file_md5.append(item)
                    # else:
                    #     clear_file.append(item)
        # conditions = [
        #     f"ID проверки: {uuid.uuid4()}\n",
        #     f"Проверено {len(file_hashes)} файлов\n",
        #     f"Вирусов обнаружено: {len(virus_file)}" if len(virus_file) > 0 else f"Вирусов нет\n"
        # ]
        # return " ".join(conditions)


    #############################################
    #                  SHA256                   #
    #############################################
    def get_sha256_hashes(self):
        files = self.get_files_from_dirs()
        sha256_hashes = []
        for file in files:
            try:
                with open(file, "rb") as file:
                    bytes = file.read()
                    sha256_hash_file = hashlib.sha256(bytes).hexdigest()
                    sha256_hashes.append(sha256_hash_file)
            except FileNotFoundError as err:
                ...
        return sha256_hashes

    def sha256_hash_checker(self):
        clear_file = []
        virus_file = []
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\SHA256.txt"
        file_hashes = self.get_sha256_hashes()
        with open(path, "r") as file:
            hashes = file.read().split()
            for hash in hashes:
                for item in file_hashes:
                    if hash == item:
                        virus_file.append(item)
                    else:
                        clear_file.append(item)
        return len(virus_file) if len(virus_file) > 0 else "Вирусов нет!"

    #############################################
    #                  SHA1                     #
    #############################################
    def get_sha1_hash(self):
        files = self.get_files_from_dirs()
        sha1_hashes = []
        for file in files:
            try:
                with open(file, "rb") as file:
                    bytes = file.read()
                    sha1_hash_file = hashlib.sha1(bytes).hexdigest()
                    sha1_hashes.append(sha1_hash_file)
            except FileNotFoundError as err:
                ...
        return sha1_hashes


    def sha1_hash_checker(self):
        clear_file = []
        virus_file = []
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\SHA1_HASHES.json"
        file_hashes = self.get_sha1_hash()
        with open(path, "r") as file:
            res = json.load(file)
            for value in res["data"]:
                data = value["hash"]
                for hash in file_hashes:
                    if hash == data:
                        virus_file.append(hash)
                    else:
                        clear_file.append(hash)
        return len(virus_file) if len(virus_file) > 0 else "Вирусов нет!"

    def start(self):
        thread = threading.Thread(target=self.md5_hash_checker)
        thread.start()
        thread.join()

    def main(self):
        self.start()
        conditions = [
            f"ID проверки: {uuid.uuid4()}\n",
            f"Проверено {len(self.virus_file_md5)} файлов\n",
            f"Вирусов обнаружено: {len(self.virus_file_md5)}:\n{', '.join(self.virus_file_md5)}" if len(self.virus_file_md5) > 0 else f"Вирусов нет\n"
        ]

        return " ".join(conditions)


if __name__ == '__main__':
    gc.collect()
    t = AntivirusEngine()
    print(t.md5_hash_checker())


