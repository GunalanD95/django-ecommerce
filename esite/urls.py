from django.urls import path , include
from .  import views
from . views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('accounts/', include('allauth.urls')),
]