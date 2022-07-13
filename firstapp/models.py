from django.db import models

# Create your models here.

class items(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'img')
    des = models.TextField()
    price = models.IntegerField()
    offerprice = models.IntegerField()
    code = models.IntegerField()


class category(models.Model):
    img = models.ImageField(upload_to = 'img')
    name = models.CharField(max_length=100)
    totalitem = models.IntegerField()