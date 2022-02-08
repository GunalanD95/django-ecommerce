from .models import * 

def message_processor(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = SaleOrder.objects.get_or_create(customer=customer , complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    return {
        'cartItems':cartItems,
    }