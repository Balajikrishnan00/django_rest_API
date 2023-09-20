from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from .models import Users


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def users_view(request):
    if request.method == 'GET':
        queryset = Users.objects.all()
        serializers = UserSerializers(queryset, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        data = request.data
        serializers = UserSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    elif request.method == 'PUT':
        data = request.data
        serializers = UserSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    elif request.method == 'PATCH':
        data = request.data
        queryset = Users.objects.get(id=data['id'])
        serializers = UserSerializers(queryset, data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    elif request.method == 'DELETE':
        data = request.data['id']
        queryset = Users.objects.get(id=data)
        queryset.delete()
        return Response({"message": "data Deleted"})
