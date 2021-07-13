from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):

    return HttpResponse(reverse('model:index'))

def login(request):
    print('请求方法：',request.method)
    print('path:',request.path)
    print('path_info:',request.path_info)
    print('GET:',request.GET)
    print('POST:',request.POST)
    return render(request,'model/login.html')