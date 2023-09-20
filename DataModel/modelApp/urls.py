from django.urls import path, include
from .views import index_view, loginView, StudentsAPI, EmployeeViewSet, RegisterApi, UserTokenApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'employee', EmployeeViewSet, 'employee')

# urlpatterns = router.urls

urlpatterns = [
    path('index/', index_view),
    path('login/', loginView),
    path('students/', StudentsAPI.as_view()),
    path('', include(router.urls)),
    path('register/', RegisterApi.as_view()),
    path('token/', UserTokenApi.as_view())



]
