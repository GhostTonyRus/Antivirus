import hashlib
import json
import os


class AntivirusEngine:
    def __init__(self, file=None):
        self.filename = file
        self.dirs = {
            "antivirus": "C:\\PycharmProjects\\Antivirus\\antivirus_package",
            "database": "C:\\PycharmProjects\\Antivirus\\database_package",
            "server": "C:\\PycharmProjects\\Antivirus\\server_package",
            "logging": "C:\\PycharmProjects\\Antivirus\\logging_package"
        }

    def get_files_from_dirs(self):
        """возвращает все файлы из директории"""
        files = []
        for value in self.dirs.values():
            files.append(value)
        # files = []
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package"
        # for item in files:
        #     for dirpath, dirnames, filenames in os.walk(item):
        #         for file in filenames:
        #             files.append(file)
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                if file.endswith(".py"):
                    files.append(file)
        return files[4:]
        # print(files[4:])
    #############################################
    #                   MD5                     #
    #############################################
    def get_md5_hashes(self):
        files = self.get_files_from_dirs()
        md5_hashes = []
        for file in files:
            try:
                with open(file, "rb") as file:
                    bytes = file.read()
                    md5_hash = hashlib.md5(bytes).hexdigest()
                    md5_hashes.append(md5_hash)
            except FileNotFoundError as err:
                ...
        return md5_hashes

    def md5_hash_checker(self):
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\MD5 Virus Hashes.txt"
        file_hashes = self.get_md5_hashes()
        clear_file = []
        virus_file = []
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


    def main(self):
        files = []
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package"
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                files.append(file)
        print(files)


if __name__ == '__main__':
    a = AntivirusEngine()
    print(a.get_sha1_hash())
    print(a.sha1_hash_checker())

# from pathlib import Path
# res = main().split("\\")
# p = Path("\\".join(res))
# with open(p, "rb") as file:
# try:
#     h = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\bootTel.dat"
#     with open(rf"{h}", "rb") as file:
#         res = file.read()
#         hash = hashlib.sha1(res).hexdigest()
#         print(hash)
# except FileNotFoundError as err:
#     ...
# finally:
#     print("dfsf")
