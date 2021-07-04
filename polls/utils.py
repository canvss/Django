# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/4 20:32
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
import hashlib
import random

from polls import captcha

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()

def gen_random_code(length=4):
    return ''.join(random.choices(ALL_CHARS,k=length))

