from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import * 
from django.contrib import auth
from .models import *
from pdapp.models import * # 외부키로쓰는 클래스 import 하려고

# Create your views here.

#로그인
def login(request): 
    if request.method =='POST': #post방식이면
        username = request.POST['username'] #유저네임 받고
        password = request.POST['password'] #pw받고
        user = auth.authenticate(request, username = username, password = password)
        if user is not None : #유저가 있으면
            auth.login(request, user) #유저정보로 로그인
            return redirect('index') #인덱스페이지로 redirect
        else:
            return render(request, 'login.html', {'error' : '아이디나 비번이 틀렸어!'})
            #틀렸을 때
    else:
        return render(request, 'login.html') #post방식 아닐 때

#회원가입
def signup(request):
    if request.method == 'POST' :
        if request.POST['password'] == request.POST['re_password']: 
            if request.POST['gender'] == '1':
                gen = True
            else:
                gen = False

            user = User.objects.create_user(
                username=request.POST['username'], 
                password = request.POST['password'],
                address = request.POST['address'],
                phone = request.POST['phone'],
                gender = gen,
                age = request.POST['age'],
                ) #사용자정보 post로 받고
            auth.login(request, user) #자동 로그인
            return redirect('signup_done') #인덱스 page로
        return render(request, 'signup.html', {'error': '비밀번호가 틀립니다.'}) #pw <> repw 일때
    return render(request, 'signup.html') #post아닐때

#회원가입 완료
def signup_done(request):
    return render(request, 'signupdone.html')
    
#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('login')

# 마이페이지
def mypage(request):
    # 로그인 되어있으면 myapge.html 접근
    if request.user.is_authenticated:
        return render(request,'mypage.html')
    # 아니라면 로그인페이지 접근
    else :
        return redirect('login')


def myinfo(request):
    return render(request,'myinfo.html')

#내리뷰
def myreview(request, pk):
    user = get_object_or_404(User, pk=pk)
    content = Review.objects.all()
    return render(request, 'myreview.html', {'user':user})

#구매상품
def myitem(request):
    #user = get_object_or_404(User, pk = pk) #pk받으면 로그인한사람 구분 가능 (ex 3번)
    item = MyProduct.objects.filter(User = request.user) #myproduct 주인이 로그인한사람인것 불러오기 => 이거 하면 오류나는데 안해도되는건가?;;
    return render(request, 'myitem.html', {
        'item': item
        })

#내 사진
def mypic(request):
    pic = Album.objects.filter(user = request.user) #myproduct 주인이 로그인한사람인것 불러오기 => 이거 하면 오류나는데 안해도되는건가?;;
    return render(request, 'mypic.html', {
        'pic': pic
        })

# if request.method == 'POST':
#         guestname = request.user #로그인한사람
#         guest_text = request.POST['guest_text']
#         receiver_name = cyuser #미니홈피 주인 (받는 사람)

#         guestbooks = Guestbook() #새로운 객체를 만들겠다

#         guestbooks.guestname = guestname
#         guestbooks.guest_text = guest_text
#         guestbooks.receiver_name = receiver_name
#         guestbooks.save()
#         return render(request, 'main/guest_detail.html',{
#             'cyuser':cyuser,
#             'guestbook':guestbook
#         })
#     else:
#         return render(request,'main/guest_detail.html',{
#             'cyuser':cyuser,
#             'guestbook':guestbook
#         })

# def updateProfile(request):
#     if request.method == 'POST' and 'imgs' in request.FILES:
#         user = request.user
#         contents = request.POST['contents']
#         imgs = request.FILES['imgs']
#         user.profile_img = imgs
#         user.contents = contents
#         user.save()
#         return render(request,'main/updateProfile.html', {'done':'사진과 소개가 업데이트 되었습니다.'})
#     elif request.method == 'POST':
#         user = request.user
#         contents = request.POST['contents']
#         user.contents = contents
#         user.save()
#         return render(request,'main/updateProfile.html', {'done':'소개가 업데이트 되었습니다.'})
#     return render(request,'main/updateProfile.html')