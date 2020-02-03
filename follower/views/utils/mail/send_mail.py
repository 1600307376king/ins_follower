#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 18:40
# @Author  : HelloWorld
# @File    : send_mail.py

from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.shortcuts import render, HttpResponse

import json


def send_email(recipient, code):
    res = send_mail('注册通知', '验证码：{}'.format(code), '1600307376@qq.com', [recipient])
    if res == 1:
        return '邮件发送成功'
    else:
        return '邮件发送失败'