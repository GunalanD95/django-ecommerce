from django.db import models
from django.conf import settings
# Create your models here.


class OrderCart(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item_name = models.ForeignKey(OrderCart, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    order_item = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username
