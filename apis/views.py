from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from esite.models import *
from .serializers import CustomerSerializer
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def customer_list(request):

    if request.method == 'GET':
        customer = Customer.objects.all()
        # serialize the model data using the serializer which we created
        serialzer = CustomerSerializer(customer, many=True)
        return JsonResponse(serialzer.data , safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialzer = CustomerSerializer(data=data)

        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data , status=201)
        return JsonResponse(serialzer.errors,status=400)