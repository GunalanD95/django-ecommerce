from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from esite.models import *
from .serializers import CustomerSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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