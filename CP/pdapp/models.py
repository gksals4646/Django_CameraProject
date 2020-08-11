from django.db import models
from django.contrib.auth.models import AbstractUser
# from userapp.models import User

# Create your models here.
class LensType(models.Model):
    lname=models.CharField(max_length=200, null=True)

class BodyType(models.Model):
    filmb=models.CharField(max_length=200, null=True)
    digitalb=models.CharField(max_length=200, null=True)

class Brand(models.Model):
    bname = models.CharField(max_length=50, null=True)

class Product(models.Model):
    pdname = models.CharField(max_length = 100, null = True)
    brand = models.CharField(max_length = 100, null = True)
    price =   models.IntegerField(null = True)
    pic = models.ImageField(null = True, upload_to="%Y/%m/%d")
    star = models.IntegerField(null = True) #별점
    bodytype = models.ForeignKey(BodyType, null = True , on_delete = models.CASCADE)
    lenstype = models.ForeignKey(LensType, null = True , on_delete = models.CASCADE)



