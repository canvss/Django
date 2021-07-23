# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/15 21:15
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from django.contrib import admin
from django.urls import path, re_path,include
from ORM import views

urlpatterns = [
    path('index/',views.index),
    path('add/',views.add)
]
