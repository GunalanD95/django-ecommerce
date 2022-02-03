from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'esite/home.html')

def shop(request):
    return render(request, 'esite/shop.html')

def product(request):
    return render(request, 'esite/product.html')

def about(request):
    return render(request, 'esite/about.html')

def contact(request):
    return render(request, 'esite/contact.html')
