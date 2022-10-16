from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import path

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
from .forms import CreateUserForm

def home(request):
    return render(request, 'userlogin/dashboard.html')

def map(request):
    return render(request, 'userlogin/map.html')

def about(request):
    return HttpResponse('About')

def customer(request):
    return HttpResponse('Customer')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'userlogin/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'userlogin/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')