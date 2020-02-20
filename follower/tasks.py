#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 22:06
# @Author  : HelloWorld
# @File    : tasks.py
"""
暂时发现需要加--pool=solo 参数才能发送邮件
celery -A ins_follower -l info -n celeryMan --pool=solo

"""
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .views.utils.mail.send_mail import send_email


@shared_task
def add_send_email(recipient, code):
    msg = send_email(recipient, code)
    return msg


@shared_task
def add(x, y):
    return x + y