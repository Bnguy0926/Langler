from django.http import HttpRequest, HttpResponse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('map/', views.map),
    path('about/', views.about),
    path('customer/', views.customer),
]