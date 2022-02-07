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
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = SaleOrder.objects.get_or_create(customer=customer , complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'esite/cart.html',context)

# def add_to_cart(self,product_id):
