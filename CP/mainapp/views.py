from django.shortcuts import render
from .models import Product

# Create your views here.

# 메인 페이지
def index(request):
    return render(request, 'index.html')

# 상품 페이지
def item_body(request):
    product_body = Product.objects.filter(bodytype='1')
    return render(request, 'item_body.html', {'product_body':product_body})

def item_lens(request):
    product_lens = Product.objects.filter(bodytype='2')
    return render(request, 'item_lens.html', {'product_lens':product_lens})


# 랭킹 페이지
def rank(request):
    return render(request, 'rank.html')

# 사진첩 페이지
def album(request):
    return render(request, 'album.html')