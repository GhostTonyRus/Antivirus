import smtplib
import uuid
import string
import random
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

###


class Two_factor_authentication:
    def __init__(self):
        # self.data_base = OfficerDatabase("customs_officers")
        ...

    def login_to_the_system(self, login, password):
        count = 0
        message, code = self.message
        user_login = login
        user_password = str(password)
        # if self.data_base.check_data("customs_officers_users", user_login, user_password):
        #     print("Аутентификация пройдена!")
        #     try:
        #         self.send_email(email="antonmakeev18@gmail.com", msg=message)
        #         print("Письмо успешно отправлено!")
        #         while count < 5:
        #             response = input("Введите код для продолжения:\n>>>")
        #             if response == code:
        #                 print("Добро пожаловать!")
        #                 return True
        #                 # break
        #             else:
        #                 print("Неверный код! Попробуйте снова!")
        #                 count += 1
        #                 if count < 5:
        #                     continue
        #                 else:
        #                     print(f"Превышен лимит входа! Было использовано {count} попыток!")
        #                     break
        #     except Exception as err:
        #         print(err)
        #         print("Не удалось отправить письмо!")
        # else:
        #     print("Введеные неверные данные!")

    @property
    def message(self):
        code = self.generate_code()
        message = MIMEMultipart()
        text_message = f"""Two-factor authentication\nYour login code: {code}"""
        message["From"] = "From developer"
        message["To"] = ""
        message["Subject"] = "login code"
        message.attach(MIMEText(text_message, "plain"))
        return text_message, code

    def generate_code(self):
        upper_letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        digits = string.digits
        symbols = "".join([upper_letters + lower_letters + digits])
        code = "".join(random.sample(symbols, 20))
        return code

    def send_email(self, email=None, password=None, FROM=None, TO=None, msg=None):
        # рабочая почта с которой будет отправлено письмо
        work_email = "antonmakeev14@gmail.com"
        # рабочий пароль
        work_password = "nzse nmjz nioj btfl"
        # почта на которую будет отправлено письмо
        dest_email = email
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        # подключаемся к SMTP-серверу
        smtp_server.starttls()
        # входим в учётную запись
        smtp_server.login(work_email, work_password)
        # отправка электронного пиьса
        smtp_server.sendmail(work_email, dest_email, msg)
        # выходим из сервера
        smtp_server.quit()

if __name__ == '__main__':
    test = Two_factor_authentication()
    test.login_to_the_system("Admin", "Admin")
