import datetime
from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.

class category(models.Model):
    img = models.ImageField(upload_to = 'img')
    name = models.CharField(max_length=100)
    totalitem = models.IntegerField()

    def __str__(self):
        return self.name


class items(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'img')
    des = models.TextField()
    cat = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
    offerprice = models.IntegerField()
    code = models.IntegerField()


class customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)



class order(models.Model):
    items = models.ForeignKey(items, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)