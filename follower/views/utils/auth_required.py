#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 20:59
# @Author  : HelloWorld
# @File    : auth_required.py
"""
auth_required.py: a set of decorator functions
"""
from functools import wraps
from django.core.cache import cache
from django.shortcuts import redirect


# 访问权限验证，不通过则跳转登录页面
def auth_required_decoration(func):
    """
    a decorator that detects session_id on access
    :param func: view function
    :return: function
    """
    @wraps(func)
    def wrap(req):
        if req.COOKIES.get('session_id') and req.COOKIES.get('user_id'):
            user_session_id = cache.get(str(req.COOKIES.get('user_id')))
            if user_session_id == req.COOKIES.get('session_id'):
                return func(req)
        return redirect('/login/')

    return wrap
