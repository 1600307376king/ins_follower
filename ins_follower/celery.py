#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 22:16
# @Author  : HelloWorld
# @File    : celery.py
from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ins_follower.settings')

app = Celery('ins_follower')

app.config_from_object('django.conf:settings', namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks()  # 发现任务文件每个app下的task.py


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))