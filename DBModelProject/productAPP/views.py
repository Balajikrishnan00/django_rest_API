from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Product
from django.forms.models import model_to_dict


# Create your views here.

def apiHome(request):
    model_data = Product.objects.all().order_by('?').first()
    # model_data = Product.objects.all()
    data = {}
    if model_data:
        # data = model_to_dict(model_data,fields=['id','title'])
        data = model_to_dict(model_data, )
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # ata['price'] = model_data.price
        return JsonResponse(data)
    #return HttpResponse(data, headers={'content-type': 'application/json'})
