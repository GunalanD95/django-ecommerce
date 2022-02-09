from rest_framework import serializers

from esite.models import SaleOrder,ProductCategory,Product,SaleOrder,OrderItem,ShippingAddress, Customer
from django.contrib.auth.models import User



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
