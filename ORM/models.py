from django.db import models

# Create your models here.

class Book(models.Model):
    no = models.AutoField(primary_key=True,verbose_name="no")
    title = models.CharField(max_length=32,unique=True) #unique唯一性
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8,decimal_places=2)  #999999.99
    press = models.CharField(max_length=32)
