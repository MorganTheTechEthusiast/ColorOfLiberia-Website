from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("explore/", explore, name="explore"),
    path("business_details/", business_details, name="business_details"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
     

]