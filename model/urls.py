# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/13 21:59
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from django.urls import re_path, path
from model import views

urlpatterns = [
    re_path(r'^index/',views.index,name='index'),
    path('login/',views.login),
]