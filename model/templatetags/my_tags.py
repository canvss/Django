# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/14 22:41
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from django import template

register = template.Library()

@register.filter
def multi_filter(x,y):
    return x*y

@register.simple_tag
def multi_tag(x,y,z):
    return x*y*z