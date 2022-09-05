from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import Employee
from.serializer import Employee_serializer

class Basic_auth(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_serializer

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]
