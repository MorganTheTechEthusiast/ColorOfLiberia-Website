from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    page_title = "Home"

    Context = {
        "page_title": page_title,

    }

    return render(request, "home.html", Context)

def about(request):

    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def explore(request):
    all_businesses = Business.objects.prefetch_related('media')

    context = {
        "all_businesses": all_businesses,
        "page_title": "Explore Businesses",
    }
    return render(request, "explore.html", context)

def blog(request):
    return render(request, "blog.html")


def faq(request):
    return render(request, "faq.html")

def business_details(request):
    return render(request, "business_details.html")

