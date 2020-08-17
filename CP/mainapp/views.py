from .models import Product
from django.shortcuts import render,redirect,get_object_or_404
from .models import Album,Review
from pdapp.models import *
from django.db.models import Avg

# Create your views here.

# 메인 페이지
def index(request):
    return render(request, 'index.html')

# 상품 페이지
def item_body(request):
    product = Product.objects.all()
    product_body = Product.objects.filter(lenstype=None)

    stars = Star.objects.values('pdname').annotate(Avg('star'))
    avg_star = {}
    
    for star in stars:
        pdname = Product.objects.get(pk=star['pdname'])
        avg_star[pdname.pdname] = star['star__avg'] 

    return render(request, 'item_body.html', {'product_body':product_body, 'stars':stars, 'avg_star':avg_star, 'product':product})

def item_lens(request):
    product_lens = Product.objects.filter(bodytype='2')
    return render(request, 'item_lens.html', {'product_lens':product_lens})

# 랭킹 페이지
def rank(request):
    return render(request, 'rank.html')

# 사진첩 페이지
def album(request):
    return render(request, 'album.html')


def item(request):
    return render(request, 'item.html')


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

# 사진 삭제 함수
def delete_album(request):
    album_id = request.GET['album_id'] # 삭제 버튼을 눌렀을 때 album_id 를 받아옴
    album = Album.objects.get(id=album_id) # models 의 Album 중 id 가 같은 것을 가져옴
    album.delete() # 삭제
    return redirect('album')

def search(request):
    album = Album.objects.all()
    search_body = request.GET['search_name'] 
    search_lens = request.GET['search_name']
    search_brand = request.GET['search_name']
    albums_body = album.filter(bodypd__filmb__icontains=search_body)
    albums_lens = album.filter(lenspd__lname__icontains=search_lens)
    # albums_brand = album.filter(brandpd__icontains=search_brand)

    if albums_body:
        albums = album.filter(bodypd__filmb__icontains=search_body)
        return render(request, 'search_list.html', {'albums':albums})

    elif albums_lens:
        albums = album.filter(lenspd__lname__icontains=search_lens)
        return render(request, 'search_list.html', {'albums':albums})

    # elif albums_brand:
    #     albums = album.filter(brandpd__icontains=search_brand)
    #     return render(request, 'search_list.html', {'albums':albums})
    
    else:
        return redirect('album')

def album_detail(request,pk):
    album = Album.objects.filter(pk=pk)
    return render(request,'album_detail.html',{'album' : album })


#제품 상세 페이지
def item_detail(request,pk):
    item = Product.objects.filter(pk=pk) #class에서 product pk로 불러옴
    return render(request, 'item_detail.html', {'item' : item })
