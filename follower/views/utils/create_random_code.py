#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 19:04
# @Author  : HelloWorld
# @File    : create_random_code.py
import random


def get_random_set(bits):
    num_set = [chr(i) for i in range(48, 58)]

    char_set = [chr(i) for i in range(65, 90)]

    total_set = num_set + char_set

    value_set = "".join(random.sample(total_set, bits))

    return value_set
