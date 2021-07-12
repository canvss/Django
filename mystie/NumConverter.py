# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/7/12 22:40
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
# 自定义一个NumConverter转换器

class NumConverter:
    regex = '[0-9]{2}'
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        pass