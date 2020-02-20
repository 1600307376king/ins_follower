#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 17:52
# @Author  : HelloWorld
# @File    : sign_in.py
"""
this module includes login, register and detection the input
"""
import os
import json
import hashlib
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from follower.models import User
from follower.tasks import add_send_email
from ..utils.reg_match import choice_ph_or_email
from ..utils.create_random_code import get_random_set
from ..utils.check_login_register import check_format
from follower.views.utils.encryption import sha1_encryption


# 注册
def register(request):
    """
    if the request method equals post, Send email about the captcha, and save data to redis
    :param request:
    :return: register.html
    """
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))
        res = {'msg': 'Email has been send'}
        if check_format(dic) == 'Format input correctly':
            random_code = get_random_set(6)
            dic.update({'auth_code': random_code})
            cache.set(dic['first_input'], dic, timeout=60 * 60)
            add_send_email.delay(dic['first_input'], random_code)
            res['msg'] = 'Format input correctly'
        return JsonResponse(res)

    return render(request, 'register/register.html')


# 检测输入账号是否存在
def get_tk(request):
    """
    check account or phone number or email address, this check_format function Check if them exists
    and their format
    :param request:
    :return: json
    """
    res = dict()
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))
        res = {'error_msg': check_format(dic)}
    return JsonResponse(res)


# 检测验证码是否正确
def auth_email_or_phone(request, i):
    """
    this function check the format of address or phone number, compare with the captcha
    saved in redis
    :param request:
    :param i: email address or phone number
    :return:
    """
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))
        msg = dict()
        storage_dic = cache.get(i, '')
        if dic.get('type', '') != 'resend':
            msg['msg'] = 'Verification code error'
            if storage_dic and storage_dic.get('auth_code') == dic['auth_code']:
                msg['msg'] = 'Input format error'
                user_account = storage_dic.get('account', '')
                password = storage_dic.get('password', '')
                nickname = storage_dic.get('nickname', '')
                first_inp = choice_ph_or_email(storage_dic.get('first_input', ''))
                email = first_inp[0].group() if first_inp[0] else ''
                phone_number = first_inp[1].group() if first_inp[1] else ''
                if first_inp or phone_number:
                    enc_pwd = sha1_encryption(password)
                    msg['msg'] = 'Verification successful'
                    User.objects.create(account=user_account, password=enc_pwd, nickname=nickname,
                                        phone_number=phone_number, email=email)
                    cache.delete(i)
            return JsonResponse(msg)

        random_code = get_random_set(6)
        storage_dic['auth_code'] = str(random_code)
        add_send_email.delay(i, random_code)
        msg['msg'] = 'Email has been send'
        return JsonResponse(msg)

    return render(request, 'register/register.html')


# 登录
def my_login(request):
    """
    login function, verify account and password, and then return a token
    :param request:
    :return:
    """
    if request.method == 'POST':
        dic_data = request.body
        dic = json.loads(dic_data.decode('utf-8'))
        ph_em_ac = choice_ph_or_email(dic.get('first_input', ''))
        msg = dict()
        if ph_em_ac[0]:
            email = ph_em_ac[0].group()
            query_obj = User.objects.filter(email=email).first()
            if query_obj:
                if query_obj.password == dic.get('password', ''):
                    msg['msg'] = 'Login successful'
                    msg['id'] = query_obj.id

        elif ph_em_ac[1]:
            query_obj = User.objects.filter(phone_number=ph_em_ac[1].group()).first()
            if query_obj:
                if query_obj.password == dic.get('password', ''):
                    msg['msg'] = 'Login successful'
                    msg['id'] = query_obj.id
        elif ph_em_ac[2]:
            query_obj = User.objects.filter(account=ph_em_ac[2].group()).first()
            if query_obj:
                if query_obj.password == dic.get('password', ''):
                    msg['msg'] = 'Login successful'
                    msg['id'] = query_obj.id
        else:
            msg['msg'] = 'Input format error'

        if msg.get('msg', '') == 'Login successful' and msg.get('id', ''):
            token = hashlib.sha1(os.urandom(24)).hexdigest()
            msg['token'] = token
            cache.set(str(msg['id']), token, timeout=60 * 60 * 24 * 2)
        return JsonResponse(msg)
    return render(request, 'register/login.html')
