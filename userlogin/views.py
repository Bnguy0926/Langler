from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import path

# Create your views here.

def home(request):
    return render(request, 'userlogin/dashboard.html')

def about(request):
    return HttpResponse('About')

def customer(request):
    return HttpResponse('Customer')

def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'userlogin/register.html', context)

def loginPage(request):
    form = UserCreationForm()
    context = {}
    return render(request, 'accounts/login.htlml', context)