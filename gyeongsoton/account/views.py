from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, CustomAuthForm
from django.contrib import messages
from gyeongsoton import *
from account.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = CustomAuthForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR,
                                 " 가입하지 않은 계정이거나, 잘못된 비밀번호입니다")
            return redirect("login")
    else:
        form = CustomAuthForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user = CustomUser.objects.get(username=request.user)
            if(user.sex == "남"):
                if(user.age == "5"):
                    user.profile = "static/img/5b.png"
                elif(user.age == "10"):
                    print('남10')
                elif(user.age == "20"):
                    print('남20')
                elif(user.age == "30"):
                    print('남30')
                elif(user.age == "40"):
                    print('남40')
                elif(user.age == "50"):
                    print('남50')
            else:
                if(user.age == "5"):
                    print('여5')
                elif(user.age == "10"):
                    print('여10')
                elif(user.age == "20"):
                    print('여20')
                elif(user.age == "30"):
                    print('여30')
                elif(user.age == "40"):
                    print('여40')
                elif(user.age == "50"):
                    print('여50')
            user.save()

            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "signup.html", {"form": form})
