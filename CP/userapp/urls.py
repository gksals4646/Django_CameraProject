from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('signup_done/', views.signup_done, name = 'signup_done'),
    path('logout/', views.logout, name = 'logout'),
    path('mypage/', views.mypage, name = 'mypage'),
    #path('mypic/', views.mypic, name = 'mypic'),
    #path('myreview/', views.myreview, name = 'myreview'),
    #path('myitem/', views.myitem, name = 'myitem'),
    #path('myinfo/', views.myinfo, name = 'myinfo'),
    
    
]