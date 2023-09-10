import smtplib
import string
import random
from email.mime.text import MIMEText
from email.header import Header

class Two_factor_authentication:
    def __init__(self):
        self.work_email = "antonmakeev14@gmail.com"

    def generate_code(self):
        upper_letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        digits = string.digits
        symbols = "".join([upper_letters + lower_letters + digits])
        code = "".join(random.sample(symbols, 20))
        return code

    def message(self, receiver, code):
        text = f"код потверждения:\n\n{code}"
        subject = "Двухфакторная аутентификация"
        message = MIMEText(text, "plain", "utf-8")
        message["Subject"] = Header(subject, "utf-8")
        message["From"] = self.work_email
        message["To"] = receiver
        return message.as_string()

    def send_email(self, email=None, code=None):
        # рабочая почта с которой будет отправлено письмо
        work_email = ""
        # рабочий пароль
        work_password = ""
        # почта на которую будет отправлено письмо
        receiver = email
        # создаём сообщение
        message = self.message(receiver, code)
        # активируем почтовый сервер
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        # подключаемся к SMTP-серверу
        smtp_server.starttls()
        # входим в учётную запись
        smtp_server.login(work_email, work_password)
        # отправка электронного пиьса
        smtp_server.sendmail(work_email, receiver, message)
        # выходим из сервера
        smtp_server.quit()


if __name__ == '__main__':
    test = Two_factor_authentication()
    # test.send_email("anton.makeev.2015@mail.ru", msg="hello")
