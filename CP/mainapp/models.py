from django.db import models
from django.contrib.auth.models import AbstractUser
from userapp.models import User
from pdapp.models import *

# Create your models here.

class Review(models.Model):
    product =  models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date  = models.DateField(null = True, auto_now=True) #리뷰 쓴 날짜
    content  = models.TextField(null = True)
    star= models.IntegerField(null = True) #별점

class Album(models.Model): #사진첩
    bodypd = models.ForeignKey(BodyType , null = True, on_delete = models.CASCADE) #카메라바디본체,종류
    lenspd = models.ForeignKey(LensType , null = True, on_delete = models.CASCADE)
    date = models.DateField(null = True, auto_now=True)
    pic = models.ImageField(null = True, upload_to="%Y/%m/%d")
    user = models.ForeignKey(User,on_delete=models.CASCADE)