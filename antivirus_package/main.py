import time

# from .activity_registration import Monitor
from .information_about_the_system import InfoSystem

class Antivirus:
    def __init__(self):
        pass

    def main(self):
        manual = """
        +----------------------------------------+
        | 1 | просмотр программной активности    |
        +----------------------------------------+
        | 2 | проверка файл на наличие вирусов   |
        +----------------------------------------+
        | 3 | проверка флешки                    |
        +----------------------------------------+
        | 4 | информация о системе               |
        +----------------------------------------+
        | 5 | сканер портов                      |
        +----------------------------------------+
        | 6 | заблокировать сайт                 |
        +----------------------------------------+
        | exit/0 | выйти из Антивируса           |
        +----------------------------------------+\n
        >>>
        """
        while True:
            response = str(input(manual))
            operations = ["creation", "operation", "deletion", "modification"]
            if response == "1":
                que = input("""Какой дейсвтие хотите отслеживать:
                1. Создание -> creation;
                2. Операция -> operation;
                3. Уничтожение -> deletion;
                4. Модификация -> modification;
                Для выхода из модуля введите "exit":
                Для активации напиши на английском языке операцию
                \n>>>""")
                while True:
                    if que not in operations:
                        print("Такой операции нет в списке!\nПопробуйте снова")
                    elif que == "exit":
                        print("Выходим из модуля...")
                        break
                    elif que in operations:
                        # monitor = Monitor(str(que))
                        # monitor.main()
                        print("Монитор пока не работает!")
                        break
                    else:
                        print("Такой операции нет в списке")
            elif response == "2":
                pass
            elif response == "3":
                pass
            elif response == "4":
                info = InfoSystem()
                info.main()
            elif response == "5":
                pass
            elif response == "6":
                pass
            elif response == "exit" or response == "0":
                print("завершение работы с Антивирусом")
            else:
                print("Такой цифры нет в списке")