from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee_view
from.serializer import Emp_serializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import TokenAuthentication

class Token_base(ModelViewSet):
    queryset = Employee_view.objects.all()
    serializer_class = Emp_serializer

    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]
