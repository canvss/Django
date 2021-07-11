from datetime import datetime
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
    return render(request, 'mystie/index.html', {'fruits':selected_fruits})

def get_time(request):
    time = datetime.now()
    return render(request,'mystie/time.html',{'time':time})

def show_weather(request):
    pass

def year_archive(request,year):
    print(year)
    return HttpResponse(year)

def year_month(request,year,month):
    return HttpResponse(year+'年'+month+'月')


def year_month_day(request,year,month,day):
    print('%s年%s月%s日',{year,month,day})
    return HttpResponse(year+'年'+month+'月'+day+'日')