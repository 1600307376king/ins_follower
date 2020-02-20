#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 12:50
# @Author  : HelloWorld
# @File    : reg_match.py
"""
***
"""

import re


def choice_ph_or_email(req):
    """
    matching input type
    :param req: input
    :return:
    """
    email = re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.(com|cn|net)$', req)
    phone_number = re.search(r'^(13[0-9]|14[5-9]|15[0-35-9]|166|17[0-8]|18[0-9]|19[89])[0-9]{8}$',
                             req)
    account = re.search(r'^[0-9A-Za-z\u4e00-\u9fa5\x21-\x7e]{6,20}$', req)
    return email, phone_number, account
