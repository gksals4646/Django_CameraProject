from django.shortcuts import render, redirect
from mainapp.models import Review
from .models import *
from django.contrib import auth

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
    
       


# # 내리뷰
# def myreview(request):
#     user = get_object_or_404(User, pk=pk)
#     content = Review.objects.filter(user = user)
#     date= 
#     star=
#     return render(request, 'myreview.html')



    #     product =  models.ForeignKey(Product, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # date  = models.DateField(null = True, auto_now=True) #리뷰 쓴 날짜
    # content  = models.TextField(null = True)
    # star= models.IntegerField(null = True) #별점
