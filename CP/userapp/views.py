from django.shortcuts import render, redirect
from django.contrib import auth #로그인 할때 사용할 라이브러리
from .models import User

# Create your views here.
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
            user = User.objects.create_user(
                username=request.POST['username'], 
                password = request.POST['password'],
                address = request.POST['address'],
                phone = request.POST['phone'],
                gender = request.POST['gender'],
                age = request.POST['age'],
                ) #사용자정보 post로 받고
            auth.login(request, user) #자동 로그인
            return redirect('signup_done') #인덱스 page로
        return render(request, 'signup.html', {'error': '비밀번호가 틀립니다.'}) #pw <> repw 일때
    return render(request, 'signup.html') #post아닐때

#회원가입 완료
def signup_done(request):
    return render(request, 'signup_done.html')
    
#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('login')


#마이페이지(로그인 상태일 때만 마이페이지 들어가는 거 허용해줌)
def mypage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: #로그인 안 되어 있으면 그냥 메인화면에 머물기
            auth.login(request, user)
            return redirect('index')
    else :
        return render(request, 'mypage.html') #로그인 되어있으면 마이페이지로 이동!


