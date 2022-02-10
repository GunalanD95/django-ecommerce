from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from numpy import delete
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from esite.models import *
from .serializers import CustomerSerializer , ProductSerializer ,SaleOrderSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


#FUNCTION BASED APIS

@api_view(['GET','POST'])
def customer_list(request):

    if request.method == 'GET':
        customer = Customer.objects.all()
        # serialize the model data using the serializer which we created
        serialzer = CustomerSerializer(customer, many=True)
        # return JsonResponse(serialzer.data , safe = False)
        return Response(serialzer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serialzer = CustomerSerializer(data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data , status=status.HTTP_201_CREATED)
        # return JsonResponse(serialzer.errors,status=400)
        return Response(serialzer.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def customer_details(request,pk):
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialzer = CustomerSerializer(customer)
        return Response(serialzer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serialzer = CustomerSerializer(customer,data=request.data)


        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_202_ACCEPTED)


# CLASS BASED API VIEWS

class ProductView(APIView):
    

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):

    def get_object(request,pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    
    def put(self,request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# GENERIC & MIXIN VIEWS

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin , mixins.CreateModelMixin ,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = SaleOrderSerializer
    queryset = OrderItem.objects.all()
    lookup_field = 'id'

    #inbuilt 
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # make sure to catch 404's below
    #     obj = queryset.get(pk=self.request.user.organisation_id)
    #     self.check_object_permissions(self.request, obj)
    #     return obj


    def get(self,request,id=None):
        if id:
            queryset = self.get_queryset()
            serializer = SaleOrderSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        # id = self.get_object(pk)
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)