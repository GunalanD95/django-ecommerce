from django.urls import path , include
from .  import views
from . views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('product/',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('accounts/', include('allauth.urls')),
]