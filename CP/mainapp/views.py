from django.shortcuts import render,redirect
from .models import Album,Review
from pdapp.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

def rank(request):
    return render(request, 'rank.html')

def album(request):
    albums=reversed(Album.objects.all()) 
    return render(request, 'album.html',{'albums':albums})

def create_album(request):
    bodypd=BodyType.objects.all()
    lenspd=LensType.objects.all()
    if 'img' in request.FILES:
        btype=BodyType.objects.get(filmb=request.POST['bodypd'])
        ltype=LensType.objects.get(lname=request.POST['lenspd'])
        album = Album()
        album.user = request.user
        album.bodypd = btype
        album.lenspd = ltype
        album.pic = request.FILES['img']
        album.save()
        return render(request,'create_album.html',{'done' :'donedone'})
    return render(request,'create_album.html',{'bodypd' : bodypd , 'lenspd' : lenspd})
