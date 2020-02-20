#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 11:10
# @Author  : HelloWorld
# @File    : test_utils.py
"""
This test module tests all modules within utils
"""
import re
import random
from faker import Faker
from django.test import TestCase
from follower.views.utils.mail.send_mail import send_email
from follower.views.utils.check_login_register import check_format
from follower.views.utils.create_random_code import get_random_set
from follower.views.utils.encryption import sha1_encryption
from follower.views.utils.reg_match import choice_ph_or_email

FK = Faker()


class TestUtilsModule(TestCase):
    """
    Utils test class
    """
    def test_check_login_register(self):
        """
        Test check_login_register module
        :return:
        """
        data = {
            'first_input': random.choice([FK.phone_number(), FK.email()]),
            'account': FK.pystr()[:20],
            'nickname': FK.name()[:20],
            'password': FK.password()[:20],
        }

        self.assertEqual(check_format(dict()), 'The input is empty')
        data1 = data
        data1['first_input'] = '1600307376@qq.com'
        self.assertEqual(check_format(data1), 'The email has been registered')
        data1['first_input'] = '15058605753'
        self.assertEqual(check_format(data1), 'The phone number has been registered')
        data1['first_input'] = FK.pystr()
        self.assertEqual(check_format(data1), 'input format Error')
        data1['first_input'] = random.choice([FK.phone_number(), FK.email()])
        data1['account'] = FK.pystr().rjust(30, 'e')
        self.assertEqual(check_format(data1), 'The account format error')
        data1['account'] = FK.pystr()[:20]
        data1['password'] = FK.pystr().rjust(30, 'e')
        self.assertEqual(check_format(data1), 'Format input error')
        self.assertEqual(check_format(data), 'The input is empty')

    def test_create_random_code(self):
        """
        Test create_random_code module
        :return:
        """
        self.assertTrue(re.search(r'^[0-9A-Za-z\u4e00-\u9fa5]{6}$', get_random_set(6)))

    def test_reg_match(self):
        """
        Test reg_match module
        :return:
        """
        self.assertTrue(choice_ph_or_email('1600307376@qq.com')[0])
        self.assertTrue(choice_ph_or_email('15058605753')[1])
        self.assertTrue(choice_ph_or_email('asdasf654')[2])

    def test_send_mail(self):
        """
        Test send_mail module
        """
        res = send_email('1600307376@qq.com', get_random_set(6))
        self.assertEqual(res, 'Email has been send')

    def test_sha1_encryption(self):
        """
        test encryption module
        :return:
        """
        res = sha1_encryption('123')
        self.assertTrue(res)
