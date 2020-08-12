from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('rank/', views.rank, name='rank'),
    path('album/', views.album, name='album'),
    path('create_album/' , views.create_album, name='create_album'),
    path('search/', views.search, name='search'),
    path('album_detail/<int:pk>', views.album_detail, name='album_detail'),

]