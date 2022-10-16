from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'userlogin/dashboard.html')

def map(request):
    return render(request, 'userlogin/map.html')

def about(request):
    return HttpResponse('About')

def customer(request):
    return HttpResponse('Customer')