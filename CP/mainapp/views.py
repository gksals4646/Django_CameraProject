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

def search(request):
    album = Album.objects.all()
    search_body = request.GET['search_name']
    search_lens = request.GET['search_name']
    search_brand = request.GET['search_name']

    if search_body:
        albums = album.filter(bodypd__filmb__icontains=search_body)
        return render(request, 'search_list.html', {'albums':albums})

    elif search_lens:
        albums = album.filter(lenspd__lname__icontains=search_lens)
        return render(request, 'search_list.html', {'albums':albums})

    # elif search_brand:
    #     albums = album.filter(brandpd__icontains=search_brand)
    #     return render(request, 'search_list.html', {'albums':albums})
    
    else:
        return redirect('album')