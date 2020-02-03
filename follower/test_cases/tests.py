from django.test import TestCase
from django.views.decorators.csrf import csrf_exempt
from follower.models import User
from faker import Faker
import random
import json
import os
import requests


# Create your tests here.
fk = Faker()

# 每个测试用例命名必须加test_， 否则无法识别
class TestModels(TestCase):

    def test_add_user_data(self):

        for i in range(100):
            account = fk.pystr()[:20]
            password = fk.password()[:20]
            nickname = fk.name()[:20]
            phone_number = fk.phone_number()[:20]
            mailbox = fk.email()[:30]
            individual_resume = fk.words()[:255]
            gender = random.choice(['male', 'female', 'Not Set'])
            User.objects.create(account=account, password=password, nickname=nickname, phone_number=phone_number,
                                mailbox=mailbox, individual_resume=individual_resume, user_gender=gender)

        self.assertTrue(User)

    def test_update_user_data(self):
        fk = Faker()
        i = 3
        User.objects.filter(id=i).update(individual_resume=' '.join(fk.words()[:255]))

    def test_update_user_avatar(self):
        f = open('./follower/static/images/avatar/img/1580524273.jpg', 'r')

        User.objects.filter(id=2).update(avatar=f.name)

    def test_update_user_city(self):

        User.objects.filter(id=2).update(city=fk.city())


class TestPosts(TestModels):

    def test_send_post(self):
        pass


class TestLoginRegister(TestModels):


    def test_register(self):

        url = 'http://127.0.0.1:8000/register/'
        data = {
            'first_input': random.choice([fk.phone_number(), fk.email()]),
            'account': fk.pystr()[:20],
            'nickname': fk.name()[:20],
            'password': fk.password()[:20],
        }

        res = requests.post(url, data)
        self.assertEqual(res.status_code, 302)



