#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 20:42
# @Author  : HelloWorld
# @File    : encryption.py
import hashlib


def sha1_encryption(pwd):
    sha1 = hashlib.sha1()
    sha1.update(pwd.encode())
    return sha1.hexdigest()
