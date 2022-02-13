from django.urls import path , include
from .import views
from .views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('product/<int:product_id>/',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/',views.addToCart,name='addToCart'),
    path('delete/<int:order_id>/',views.deleteItemcart,name='deleteItemcart'),
    path('cart/payment/',views.payment,name='payment'),
    # path('accounts/', include('allauth.urls')),
]