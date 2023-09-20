from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import PersonSerializers, LoginSerializers, StudentSerializers, EmployeeSerializers, \
    RegisterSerializers

from modelApp.models import Person, Students, Employee

from rest_framework import viewsets, status


# -------------------------------------------------------------

class RegisterApi(APIView):
    def post(self, request):
        data = request.data
        serializers = RegisterSerializers(data=data)
        if not serializers.is_valid():
            return Response({"status": False, "message": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializers.save()

        return Response(serializers.data)


# --------------------------------------------------------------------

class UserTokenApi(APIView):
    def post(self, request):
        data = request.data
        serializers = LoginSerializers(data=data)
        if not serializers.is_valid():
            return Response({"status": False, "message": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
        print(serializers.data)
        user = authenticate(username=serializers.data['username'], password=serializers.data['password'])
        print(user)
        if not user:
            return Response({"message": "User not valid"})
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"status": True, "message": "userLogin", "Tokes": str(token)}, status=status.HTTP_201_CREATED)


# -------------------------------------------------------------------

@api_view(["POST"])
def loginView(request):
    data = request.data
    serializers = LoginSerializers(data=data)
    if serializers.is_valid():
        serializers.save()
        data = serializers.validated_data
        return Response({"message": data})
    return Response(serializers.errors)


# -----------------------------------------------------
# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index_view(request, ):
    if request.method == "GET":
        queryset = Person.objects.filter(color__isnull=False)
        s = PersonSerializers(queryset, many=True)
        return Response(s.data)

    elif request.method == 'POST':
        get_data = request.data
        s = PersonSerializers(data=get_data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)

    elif request.method == 'PUT':
        get_data = request.data
        s = PersonSerializers(data=get_data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)

    elif request.method == 'PATCH':
        request_data = request.data
        model_data = Person.objects.get(id=request_data['id'])
        s = PersonSerializers(model_data, data=request_data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)

    elif request.method == 'DELETE':
        request_data = request.data
        model_data = Person.objects.get(id=request_data['id'])
        model_data.delete()
        return Response({"Data": "Deleted"})


# ----------------------------------------------------------------------

class StudentsAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, mothod=['post'])
    def mail_to_person(self, request):
        return Response({"message": "mail sent success"})

    def get(self, request):
        try:
            print(request.user)
            queryset = Students.objects.all()
            page_no = request.GET.get('page', 1)
            record_size = 2
            paginator = Paginator(queryset, record_size)
            serializers = StudentSerializers(paginator.page(page_no), many=True)

            return Response(serializers.data)
        except Exception as E:
            return Response({"status": False, "message": "invaild page"})

        # serializers = StudentSerializers(queryset, many=True)

    def post(self, request):
        data = request.data
        serializers = StudentSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    def put(self, request):
        data = request.data
        serializers = StudentSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    def patch(self, request):
        data = request.data
        query = Students.objects.get(id=data['id'])
        serializers = StudentSerializers(query, data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response()

    def delete(self, request):
        data = request.data
        query_data = Students.objects.get(id=data['id'])
        query_data.delete()
        return Response({"mgs": "deleted "})




# -----------------------------------------------------------------
# viewsets
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()

    def list(self, request, *args):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(emp_name__startswith=search)
            serializers = EmployeeSerializers(queryset, many=True)
            return Response(serializers.data, )
        return Response()
