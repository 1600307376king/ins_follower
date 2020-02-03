#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 15:00
# @Author  : HelloWorld
# @File    : check_login_register.py
from follower.models import User
import re


def check_format(dic):
    if dic['first_input']:
        if re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',
                     dic['first_input']):
            if User.objects.filter(mailbox=dic['first_input']).first():
                return '邮箱已注册'

        if re.search(r'^(13[0-9]|14[5-9]|15[0-35-9]|166|17[0-8]|18[0-9]|19[89])[0-9]{8}$',
                                     dic['first_input']):
            if User.objects.filter(phone_number=dic['first_input']).first():
                return '手机号码已注册'

    if dic['account']:
        ac = dic['account']
        if (not re.search(r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{5,20}$', ac)) or (not 6 <= len(ac) <= 20):
            return '账号格式不正确'

    if dic['password']:
        pw = dic['password']
        if (not re.search(r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{5,20}$', pw)) or (not 6 <= len(pw) <= 20):
            return '账号格式不正确'
    return '输入正确'
