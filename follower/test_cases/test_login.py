#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 17:56
# @Author  : HelloWorld
# @File    : test_login.py
"""
Sign in module
"""
import json
import random
import requests
from faker import Faker
from django.test import TestCase
from django.core.cache import cache
from follower.views.utils.create_random_code import get_random_set
from follower.models import User
from follower.views.utils.check_login_register import check_format


FK = Faker()


class TestLoginRegister(TestCase):
    """"
    Test the functions within sign_in module
    """

    def test_register(self):
        """
        test register function
        :return:
        """
        url = '/register/'
        data = {
            'first_input': random.choice([FK.phone_number(), FK.email()]),
            'account': FK.pystr()[:20],
            'nickname': FK.name()[:20],
            'password': FK.password()[:20],
        }
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        post_response = self.client.post(url, data, content_type='application/json')
        response_dict = json.loads(post_response.content)
        self.assertEqual(response_dict['msg'], 'Format input correctly')

    def test_get_tk(self):
        """
        test get_tk function
        :return:
        """
        url = '/tk/'
        data = {
            'first_input': random.choice([FK.phone_number(), FK.email()]),
            'account': FK.pystr()[:20],
            'nickname': FK.name()[:20],
            'password': FK.password()[:20],
        }
        res = self.client.post(url, data, content_type='application/json')
        res_dict = json.loads(res.content)
        self.assertTrue(res_dict.get('error_msg', ''))

    def test_auth_email_or_phone(self):
        """
        test auth_email_or_phone function
        :return:
        """
        url = '/auth/1600307376@qq.com/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        random_code = get_random_set(6)
        data = {
            'first_input': '1600307376@qq.com',
            'account': FK.pystr()[:20],
            'nickname': FK.name()[:20],
            'password': FK.password()[:20],
        }
        data.update({'auth_code': random_code})
        cache.set(data['first_input'], data, timeout=30)
        post_response = self.client.post(url, data, content_type='application/json')
        res_dict = json.loads(post_response.content)
        self.assertEqual(res_dict.get('msg'), 'Verification successful')

    def test_my_login(self):
        """
        test my_login function
        :return:
        """
        url = '/login/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = {
            'first_input': '15058605753',
            'password': '123456',
        }

        di = {
            'phone_number': '15058605753',
            'account': FK.pystr()[:20],
            'nickname': FK.name()[:20],
            'password': '123456',
        }

        User.objects.create(**di)
        obj = User.objects.filter(phone_number='15058605753').filter()
        self.assertTrue(obj)
        post_response = self.client.post(url, data, content_type='application/json')
        res_dict = json.loads(post_response.content)
        self.assertEqual(res_dict.get('msg'), 'Login successful')
        self.assertTrue(res_dict.get('token'))
        data['first_input'] = ''
        post_response = self.client.post(url, data, content_type='application/json')
        res_dict = json.loads(post_response.content)
        self.assertEqual(res_dict.get('msg'), 'Input format error')
