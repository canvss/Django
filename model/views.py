import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse



def index(request):
    name= request.POST.get('username')
    class Person(object):
        def __init__(self,name,age):
            self.name = name
            self.age = age


    jack = Person('jack',23)
    info = {'name': 'tom', 'job':'python'}
    end = Person('endless', 22)
    b = True
    person_list = [jack, end]
    p = '<h2>hello world</h2>'
    list_t = [1, 2, 6, 7, 22, 90]
    num = 10
    Django_text = 'Django是一个高级的 Python 网络框架，可以快速开发安全和可维护的网站。由经验丰富的开发者构建，Django负责处理网站开发中麻烦的部分，因此你可以专注于编写应用程序，而无需重新开发。它是免费和开源的，有活跃繁荣的社区，丰富的文档，以及很多免费和付费的解决方案。'
    ctime = datetime.datetime.now()
    size_file = '187022877772'
    person_list = []
    return render(request, 'model/index.html', locals())

def login(request):
    print('请求方法：',request.method)
    print('path:',request.path)
    print('path_info:',request.path_info)
    print('GET:',request.GET)
    print('POST:',request.POST)
    return render(request,'model/login.html')

def login2(request):
    if request.method == 'POST':
        return HttpResponse('ok')
    return render(request,'model/login2.html')