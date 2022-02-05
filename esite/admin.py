from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(SaleOrder)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
