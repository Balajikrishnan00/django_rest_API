from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students, serializers_Student


# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index(request):

    if request.method == 'GET':
        query_set = Students.objects.all()
        s = serializers_Student(query_set, many=True)
        return Response(s.data)

    elif request.method == "POST":
        data = request.data
        s = serializers_Student(data=data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)

    elif request.method == 'PUT':
        data = request.data
        s = serializers_Student(data=data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)

    elif request.method == 'PATCH':
        data = request.data
        query_set = Students.objects.get(id=data['id'])
        s = serializers_Student(query_set, data=data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)

    else: #request.method == 'DELETE':
        data = request.data
        query_set = Students.objects.get(id=data['id'])
        query_set.delete()
        return Response({"data": "DELETED"}, status=Response.status_code)
