from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from faker import Faker
from follower.models import User
from .utils.auth_required import auth_required_decoration
from .utils.mail.send_mail import send_email
from django.http import JsonResponse
from follower import tasks
from django.views.decorators.csrf import csrf_exempt
from .utils.check_login_register import check_format
import os
import json
import re


# Create your views here.


# 首页
@auth_required_decoration
def home(request):
    context = {

    }
    return render(request, 'base.html', context)


# 推荐列表
@auth_required_decoration
def home_recommend(request):
    avatar_list = User.objects.all()[:10]
    fk = Faker()
    recommend_list = [{'avatar': '/images/avatar/img/' + i.avatar, 'nickname': i.nickname, 'resume': i.individual_resume,
                       'city': i.city} for i in avatar_list]
    context = {
        'recommend_list': recommend_list,
    }
    return render(request, 'recommend_list.html', context)


def home_focus_list(request):
    context = {
        'recommend_total': 10,
    }
    return render(request, 'myfocus.html', context)


def explore_images(request):
    context = {

    }
    return render(request, 'explore.html', context)


def index(request, x, y):
    context = {
        'x': x + y,
    }
    return render(request, 'test_ht.html', context)


def account(request):
    context = {

    }
    return render(request, 'myaccount.html', context)


def test1(request):
    return HttpResponseRedirect('/ts2/?page=2')


def test2(request, i):
    print(request.get_full_path())
    return render(request, 'ts2.html')