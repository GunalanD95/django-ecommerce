from django.shortcuts import render
from .models import Product, ProductCategory , Customer , SaleOrder , OrderItem


def index(request):
    return render(request, 'esite/home.html')

def shop(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'esite/shop.html' ,context)

def product(request,product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'esite/product.html', context)

def about(request):
    return render(request, 'esite/about.html')

def contact(request):
    return render(request, 'esite/contact.html')

def cart(request):
    return render(request, 'esite/cart.html')
