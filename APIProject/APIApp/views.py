from django.shortcuts import render
from django.http import JsonResponse
import json


def home(request, *args, **kwargs):
    # return render(request, 'apiapp/index.html',)
    body = request.body  # byte str of json data
    data = {}
    print(request.GET) # url query params
    print(request.POST)

    try:
        data = json.loads(body)  # str of json data -> python dict
    except Exception as e:
        print(e)

    # print(data.keys())

    # print(request.headers)
    # print(request.headers)

    #print(request.headers)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    # data['headers'] = request.headers # TypeError: Object of type HttpHeaders is not JSON serializable
    data['content-type'] = request.content_type
    print(data)

    return JsonResponse(data)

    # return JsonResponse({"Json": 'Java script objects notation'})
