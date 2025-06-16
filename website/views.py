from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, "home.html")

def about(request):

    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blog.html")

def blog_detail(request, post_id):
    # In a real application, you would fetch the blog post from the database using post_id
    # For now, we will just render a placeholder template
    return render(request, "blog_detail.html", {"post_id": post_id})

def faq(request):
    return render(request, "faq.html")

