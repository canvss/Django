from random import sample

from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def show_index(request):
    fruits =[
        'Apple','Orange','Pitaya','Durian','Mango','Pear','Peach','Grape'
    ]

    selected_fruits = sample(fruits,3)
    #第一个参数request对象
    #第二个参数返回需要渲染静态网页名字
    #第三个返回需要渲染到页面数据
    return render(request, 'polls/index.html', {'fruits':selected_fruits})

def get_time(request):

    return render(request,'')

def show_weather(request):
    pass