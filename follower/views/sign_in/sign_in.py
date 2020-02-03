#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 17:52
# @Author  : HelloWorld
# @File    : sign_in.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..utils.check_login_register import check_format
from faker import Faker
from follower.models import User
from ..utils.mail.send_mail import send_email
from django_redis import get_redis_connection
from ..utils.create_random_code import get_random_set
from django.core.cache import cache
import json
import re


def register(request):
    context = {
        'return_msg': '',
    }
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))

        context['return_msg'] = 'fail'
        if check_format(dic) == '输入正确':
            random_code = get_random_set(6)
            dic.update({'auth_code': random_code})
            cache.set(dic['first_input'], dic)
            # mail_msg = send_email('1600307376@qq.com', random_code)

            res = {'msg': '邮件发送成功'}
            return HttpResponse(json.dumps(res), content_type='application/json')

            # User.objects.create(account=user_account, password=password, nickname=nickname, phone_number=phone_number,
            #                     mailbox=mailbox)
            #
            # return redirect('/')

    return render(request, 'register.html', context)


def get_tk(request):
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))
        res = {'error_msg': check_format(dic)}
        return HttpResponse(json.dumps(res), content_type='application/json')
    return 'fail'


def auth_email_or_phone(request, i):
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))
        msg = dict()
        if dic.get('type', '') != 'resend':
            storage_dic = cache.get(dic['first_input'], '')

            if storage_dic and storage_dic.get('auth_code') == dic['auth_code']:
                msg['msg'] = '验证成功'
                return HttpResponse(json.dumps(msg), content_type='application/json')

        else:
            random_code = get_random_set(6)
            mail_msg = send_email('1600307376@qq.com', random_code)
            if mail_msg == '邮件发送成功':
                msg['msg'] = '发送成功'
            else:
                msg['msg'] = '发送失败'
            return HttpResponse(json.dumps(msg), content_type='application/json')

    return render(request, 'register_auth.html')