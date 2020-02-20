#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 15:00
# @Author  : HelloWorld
# @File    : check_login_register.py
"""
this module check the input format
"""
import re
from follower.models import User


def check_format(dic):
    """

    :param dic: request data
    :return: check result
    """
    if dic.get('first_input') and dic.get('account') and dic.get('password'):
        if re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.(com|cn|net)$',
                     dic['first_input']):
            if User.objects.filter(email=dic['first_input']).first():
                return 'The email has been registered'

        elif re.search(r'^(13[0-9]|14[5-9]|15[0-35-9]|166|17[0-8]|18[0-9]|19[89])[0-9]{8}$',
                       dic['first_input']):
            if User.objects.filter(phone_number=dic['first_input']).first():
                return 'The phone number has been registered'
        else:
            return 'input format Error'

        account = dic['account']
        if (not re.search(r'^[0-9A-Za-z\u4e00-\u9fa5\x21-\x7e]{6,20}$', account)) \
                or (not 6 <= len(account) <= 20):
            return 'The account format error'

        password = dic['password']
        if (not re.search(r'^[0-9A-Za-z\u4e00-\u9fa5\x21-\x7e]{6,20}$', password)) \
                or (not 6 <= len(password) <= 20):
            return 'Format input error'

        return 'Format input correctly'
    else:
        return 'The input is empty'
