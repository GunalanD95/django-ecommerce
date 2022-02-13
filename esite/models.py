from turtle import title
from unicodedata import category
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Customer(models.Model):
    user_id = models.OneToOneField(User,null=True , blank=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=200 ,null=True)
    email = models.EmailField(max_length=150,null=True)


    def __str__(self):
        return self.name



    

class ProductCategory(models.Model):
    name = models.CharField(max_length=200 , null=True)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    category = models.ForeignKey(ProductCategory,null=True,blank=True , on_delete=models.CASCADE)
    variant = models.CharField(max_length=200,blank=True ,null=True)
    color = models.CharField(max_length=200,blank=True ,null=True)
    size = models.CharField(max_length=200,blank=True ,null=True)

    def __str__(self):
        return self.size + ' ' + self.color




class Product(models.Model):

    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=25, null=True)
    description = models.TextField(max_length=1000 , null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    featured = models.BooleanField(default=False,null=True , blank=True)
    product_category = models.ForeignKey(ProductCategory,null=True , blank=True , on_delete=models.CASCADE)
    digital = models.BooleanField(default=False,null=True , blank=True)
    image = models.ImageField(upload_to='product_images/', null=True , blank=True)
    # image = ResizedImageField(size=[222, 222], upload_to='product_images/', null=True , blank=True)
    brand_name = models.CharField(max_length=200 , null=True)
    variant = models.ManyToManyField(ProductVariant,null=True , blank=True )


    def __str__(self):
        return self.display_name


class SaleOrder(models.Model):
    customer = models.ForeignKey(Customer,null=True , blank=True , on_delete=models.SET_NULL)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True , blank=True)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        # total = sum([item.quantity for item in order_items])
        total = len(order_items)
        return total




class OrderItem(models.Model):
    product = models.ForeignKey(Product , null=True, blank=True , on_delete=models.SET_NULL)
    order = models.ForeignKey(SaleOrder, null=True, blank=True , on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0,null=True , blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,null=True , blank=True , on_delete=models.SET_NULL)
    order = models.ForeignKey(SaleOrder,null=True , blank=True , on_delete=models.SET_NULL)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.address
