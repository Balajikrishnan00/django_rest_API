from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product

# Create your views here.


@api_view(['GET'])
def home(requests):
    data_model = Product.objects.all().first()
    data={}
    if data_model:
        data=model_to_dict(data_model)
    return JsonResponse(data)

