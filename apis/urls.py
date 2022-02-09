from django.urls import path , include
from .import views
from .views import customer_list

urlpatterns = [
    path('customers/',views.customer_list,name='cus_list'),
]