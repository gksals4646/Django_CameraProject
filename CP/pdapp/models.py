from django.db import models
from django.contrib.auth.models import AbstractUser

# from userapp.models import User

# Create your models here.
class LensType(models.Model):#lenstype과 bodytype은 type으로 통일했습니다(바디 or 렌즈)로
    lname=models.CharField(max_length=200, null=True)#안써

class BodyType(models.Model):#안써
    filmb=models.CharField(max_length=200, null=True) #안써
    digitalb=models.CharField(max_length=200, null=True) #안써

class Brand(models.Model):
    bname = models.CharField(max_length=50, null=True)

class Type(models.Model):
    pdtype=models.CharField(max_length = 10 , null = True)
    
    def __str__(self):
        return self.pdtype

class Product(models.Model):
    pdname = models.CharField(max_length = 100, null = True)
    brand = models.CharField(max_length = 100, null = True)
    price = models.IntegerField(null = True)
    pic = models.ImageField(null = True, upload_to="%Y/%m/%d")
    # star = models.IntegerField(null = True) #별점
    pdtype = models.ForeignKey(Type,null=True, on_delete=models.CASCADE)
    # bodytype = models.ForeignKey(BodyType, null = True , blank = True,  on_delete = models.CASCADE)
    # lenstype = models.ForeignKey(LensType, null = True , blank = True,  on_delete = models.CASCADE)
    def __str__(self):
        return self.pdname


class Star(models.Model):
    pdname = models.ForeignKey(Product, on_delete = models.CASCADE)
    star = models.IntegerField(null = True)
    # num = models.IntegerField(null = True)

    class Meta:
        ordering=['-star']

