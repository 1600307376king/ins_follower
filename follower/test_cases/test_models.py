#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 17:56
# @Author  : HelloWorld
# @File    : test_models.py
"""
test database module
"""
from faker import Faker
import random
from django.test import TestCase
from follower.models import User


FK = Faker()


# 测试数据库模型
class TestModels(TestCase):

    def test_add_user_data(self):
        for i in range(100):
            account = FK.pystr()[:20]
            password = FK.password()[:20]
            nickname = FK.name()[:20]
            phone_number = FK.phone_number()[:20]
            email = FK.email()[:30]
            individual_resume = FK.words()[:255]
            gender = random.choice(['male', 'female', 'Not Set'])
            User.objects.create(account=account, password=password, nickname=nickname, phone_number=phone_number,
                                email=email, individual_resume=individual_resume, user_gender=gender)

        self.assertTrue(User)

    def test_update_user_data(self):
        i = 3
        User.objects.filter(id=i).update(individual_resume=' '.join(FK.words()[:255]))

    def test_update_user_avatar(self):
        f = open('./follower/static/images/avatar/img/1580524273.jpg', 'r')

        User.objects.filter(id=2).update(avatar=f.name)

    def test_update_user_city(self):
        User.objects.filter(id=2).update(city=FK.city())

    def test_get_user_data(self):
        data = {
            'email': '1600307376@qq.com',
            'account': FK.pystr()[:20],
            'nickname': FK.name()[:20],
            'password': '123456',
        }
        User.objects.create(**data)
        obj = User.objects.filter(email='1600307376@qq.com').first()
        self.assertTrue(obj)
