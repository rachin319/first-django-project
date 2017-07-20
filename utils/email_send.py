# -*- coding:utf-8 -*-
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from WebTest.settings import EMAIL_FROM
from random import Random

def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = gnenrate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "密码重置链接"
        email_body = "请点击下面的重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def gnenrate_random_str(randomlength):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiGgKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
