from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item_body/', views.item_body, name='item_body'),
    path('item_lens/', views.item_lens, name='item_lens'),
    path('rank/', views.rank, name='rank'),
    path('album/', views.album, name='album'),
]