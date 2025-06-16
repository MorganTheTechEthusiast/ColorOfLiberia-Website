from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("explore/", explore, name="explore"),
     

]