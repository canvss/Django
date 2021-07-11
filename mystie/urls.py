# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/11 19:31
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from django.contrib import admin
from django.urls import path, re_path

from polls.views import *
from mystie import views

urlpatterns = [
    path('hello/', views.show_index),
    path('time/',views.get_time),


    # 带正则的请求
    # 已articles开头/4位0-9数字组成结尾
    re_path(r'^articles/([0-9]{4})/$',views.year_archive),
    # 给参数设置名字 ?P<year>
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.year_month),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-31]{2})/$',views.year_month_day),
]
