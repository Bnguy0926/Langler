from django.http import HttpRequest, HttpResponse
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home),
    path('map/', views.map),
    path('about/', views.about),
    path('customer/', views.customer),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
]