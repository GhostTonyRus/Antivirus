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
    test.send_email("anton.makeev.2015@mail.ru", msg="hello")
