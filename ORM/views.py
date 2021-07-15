from django.http import HttpResponse
from ORM import models
# Create your views here.
def index(request):
    # 添加数据
    # 第一种方法
    # book = models.Book(title='JavaScript深度学习',pub_date='2008-2-3',press='人民出版社',price=79.9)
    # book.save()
    # # 第二种方法
    # book2 = models.Book.objects.create(title='Python编程导论（第2版）',pub_date='2011-7-23',press='中国邮电出版社',price=199)
    # print(book.price)
    # print(type(book))
    # 查询所有
    # book = models.Book.objects.all()
    # print(book)
    # for i in book:
    #     print(i.title)
    # print(type(book))
    # # <class 'django.db.models.query.QuerySet'>
    # print(type(book))
    # 查询filter
    # book = models.Book.objects.filter(title='设计模式')
    # print(book[0].title)
    # print(type(book))
    # 查询get 智能返回唯一一个对象
    book = models.Book.objects.get(no=2)
    print(type(book))
    print(book.title)
    return HttpResponse('ok')