from django.db import models

# Create your models here.

class Book(models.Model):
    no = models.AutoField(primary_key=True,verbose_name="no")
    title = models.CharField(max_length=32,unique=True) #unique唯一性
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8,decimal_places=2)  #999999.99
    press = models.CharField(max_length=32)


# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 与AuthorDetail建立一对一的关系
    authorDetail =  models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)

# 作者详情
class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

# 出版社详情
class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name

# 建立图书表
class Books(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='图书id') #verbose_name：详细信息
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    '''
    DecimalField
        固定精度的十进制数，在Python中表示一个 十进制的实例
        #1. DecimalField max_digits 
        　　数中允许的最大数目的数字
        #2. DecimalField decimal_places 
　           　存储的小数位数的位数   
    '''
    price = models.DecimalField(max_digits=5,decimal_places=2)


    # 与出版社表建立一对多的关系，外键字段建立在多的一方
    publish = models.ForeignKey(to='Publish',to_field='id',on_delete=models.CASCADE)

    # 与作者表建立多对多的关系，ManyToManyField可以建立在两个模型中的任意一个，自动创建第三张表
    Authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title