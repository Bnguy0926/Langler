from unicodedata import name
from django.http import HttpRequest, HttpResponse
from django.urls import include, path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name = "home"),
    path('map/', views.map),
    path('about/', views.about),
    path('customer/', views.customer),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.loginPage, name="logout"),
    path('addinfo/', views.loggedinUser, name="loggedin"),
    path('main/', views.mainPageLoggedin, name="main"),
    path('main/view/', views.randomPerson, name="random")
]