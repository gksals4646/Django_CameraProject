from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')


def signup_done(request):
    return render(request,'signup_done.html')