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
    def get_md5_hash(self):
        files = self.get_files_from_dirs()
        hashs = []
        for file in files:
            try:
                with open(file, "rb") as file:
                    bytes = file.read()
                    md5_hash = hashlib.md5(bytes).hexdigest()
                    hashs.append(md5_hash)
            except FileNotFoundError as err:
                print(err)
        return hashs

    def md5_hash_checker(self):
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\MD5 Virus Hashes.txt"
        file_hash = self.get_md5_hash()
        clear_file = []
        virus_file = []
        with open(path, "r") as file:
            hashes = file.read().split()
            for hash in hashes:
                for item in file_hash:
                    if hash == item:
                        virus_file.append(item)
                    else:
                        clear_file.append(item)
        return len(virus_file) if len(virus_file) > 0 else "Вирусов нет!"
    #############################################
    #                  SHA256                   #
    #############################################
    def get_sha256_hash(self):
        with open(self.filename, "rb") as file:
            bytes = file.read()
            sha256_hash = hashlib.sha256(bytes).hexdigest()
            return sha256_hash

    def check_sha256_file(self):
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\SHA256.txt"
        file_hash = self.get_sha256_hash()
        with open(path, "r") as file:
            hashes = file.read().split()
            for hash in hashes:
                if hash == file_hash:
                    return True
                else:
                    return False

    #############################################
    #                  SHA1                     #
    #############################################
    def get_sha1_hash(self):
        with open(self.filename, "rb") as file:
            res = file.read()
            hash = hashlib.sha1(res).hexdigest()
            return hash


    def check_sha1_file(self, file_hash):
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package\\signatures\\SHA1_HASHES.json"
        with open(path, "r") as file:
            res = json.load(file)
            for key, value in enumerate(res["data"]):
                if value["hash"] == file_hash:
                    return True
                else:
                    return False

    def main(self):
        files = []
        path = "C:\\PycharmProjects\\Antivirus\\antivirus_package"
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                files.append(file)
        print(files)
                # print(file)
                # self.test(file)

# main()
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
