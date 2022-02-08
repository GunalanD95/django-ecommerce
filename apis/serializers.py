from rest_framework import serializers

from esite.models import SaleOrder,ProductCategory,Product,SaleOrder,OrderItem,ShippingAddress


class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = '__all__'


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cart_total'] = instance.get_cart_total()
        data['total_items'] = instance.get_cart_items()
        return data