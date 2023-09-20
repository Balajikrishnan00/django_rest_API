from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializers


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def index(request):
    if request.method == 'GET':
        queryset = Person.objects.all()
        serializers = PersonSerializers(queryset, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        requestDict = request.data
        serializers = PersonSerializers(data=requestDict)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    elif request.method == 'PUT':
        requestDict = request.data
        serializers = PersonSerializers(data=requestDict)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    elif request.method == 'DELETE':
        id = request.data['id']
        queryset = Person.objects.get(id=id)
        queryset.delete()
        return Response({"Message": "Data Deleted"})

    elif request.method == 'PATCH':
        data = request.data
        queryset = Person.objects.get(id=data['id'])
        serializers = PersonSerializers(queryset, data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
