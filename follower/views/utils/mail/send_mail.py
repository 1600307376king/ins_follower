#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 18:40
# @Author  : HelloWorld
# @File    : send_mail.py
"""
the module used for send email
"""
from django.core.mail import send_mail


def send_email(recipient, code):
    """
    :param recipient: user email
    :param code: random code
    :return: send message
    """
    res = send_mail('注册通知', '验证码：{}'.format(code), '1600307376@qq.com', [recipient])
    if res == 1:
        return 'Email has been send'

    return 'Email sending failed'



