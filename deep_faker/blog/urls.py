from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('create', views.about)
]
