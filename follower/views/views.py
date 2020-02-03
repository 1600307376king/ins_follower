from django.shortcuts import render, redirect
from django.http import HttpResponse
from faker import Faker
from follower.models import User
from django.views.decorators.csrf import csrf_exempt
from .utils.check_login_register import check_format
import os
import json
import re


# Create your views here.


# 首页
def home(request):
    context = {

    }

    return render(request, 'base.html', context)


# 推荐列表
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


def index(request):

    return HttpResponse('addok')





def login(request):
    context = {

    }
    return render(request, 'login.html', context)


def account(request):
    context = {

    }
    return render(request, 'myaccount.html', context)