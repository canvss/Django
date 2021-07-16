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
    # book = models.Book.objects.get(no=2)
    # print(type(book))
    # print(book.title)

    # exclude 查询粗不匹配的数据，返回结果：QuerySet
    # book = models.Book.objects.exclude(title='设计模式')
    # <QuerySet [<Book: Book object (1)>, <Book: Book object (3)>, <Book: Book object (4)>, <Book: Book object (5)>, <Book: Book object (6)>]>
    # print(book)

    # order_by('price') 根据价格排序，正树为升序，负树为降序
    # book = models.Book.objects.order_by('-price','pub_date')
    # # 返回一个queryset对象
    # # <QuerySet [('设计模式',), ('JavaScript深度学习',), ('JAVA编程思想',), ('深入理解JVM虚拟机',), ('Python编程导论（第2版）',), ('RESTful API 设计指南',)]>
    # print(book.values_list('title'))

    # reverse() 对已经排序的QuerySet对象进行反向排序
    # book = models.Book.objects.order_by('-price').reverse()
    # print(book.values_list('title'))

    #count() 返回数据库中匹配查询(QuerySet)的对象数量。
    count = models.Book.objects.count()
    print(count)
    # first = JAVA编程思想 ,last = Python编程导论（第2版）
    first = models.Book.objects.first()
    last = models.Book.objects.last()
    # first = JAVA编程思想 ,last = Python编程导论（第2版）
    print('first = %s ,last = %s'%(first.title,last.title))

    # values()
    book = models.Book.objects.values('price')
    # <QuerySet [{'price': Decimal('89.00')}, {'price': Decimal('58.00')}, {'price': Decimal('109.00')}, {'price': Decimal('199.00')}, {'price': Decimal('79.90')}, {'price': Decimal('199.00')}]>
    print(book)

    # values_list()
    book = models.Book.objects.values_list('price')
    # <QuerySet [(Decimal('89.00'),), (Decimal('58.00'),), (Decimal('109.00'),), (Decimal('199.00'),), (Decimal('79.90'),), (Decimal('199.00'),)]>
    print(book)

    # exists()
    if models.Book.objects.exists():
        temp = 'ok'
    else:
        temp = 'NO'

    # distinct()
    book = models.Book.objects.values('price').distinct()
    print(book)
    return HttpResponse(temp)