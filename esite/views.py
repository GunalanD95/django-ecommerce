import json
from django.shortcuts import redirect, render
from .models import Product, ProductCategory , Customer , SaleOrder , OrderItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests


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
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems,
    }
    return render(request, 'esite/cart.html',context)



def addToCart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    print('Action:', action)
    print('Product:', product_id)


    customer =  request.user.customer
    product = Product.objects.get(id=product_id)
    order,created = SaleOrder.objects.get_or_create(customer=customer , complete=False)

    orderItem , created = OrderItem.objects.get_or_create(order=order , product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Success', safe=False)


def deleteItemcart(request,order_id):
    api_params = {'id':order_id}
    url = 'http://localhost:8000/apis/saleorders/{id}/'.format(**api_params)
    # apicall = requests.get(url)
    # print(apicall.url)
    # json_respons = apicall.json()
    # print('json_respons:', json_respons)

    delete = requests.delete(url)
    return redirect('cart')

def payment(request):
    return render(request, 'esite/payment.html')
