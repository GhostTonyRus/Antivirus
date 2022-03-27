import os

class Delete:
    def __init__(self, file, path):
        self.file = file
        self.path = path

    def delete_file(self):
        os.remove(self.path+self.file)
        return "Файл удалён"

    def delete_dir(self):
        os.rmdir(self.path)
        return "Директория удалена"