from django.urls import path , include
from .import views
from .views import customer_list , customer_details , ProductView , ProductDetail

urlpatterns = [
    path('customers/',views.customer_list,name='cus_list'),
    path('customers/<int:pk>',views.customer_details,name='customer_details'),
    path('products/',ProductView.as_view(),name="products-api"),
    path('products/<int:pk>',ProductDetail.as_view(),name="product-api"),
]