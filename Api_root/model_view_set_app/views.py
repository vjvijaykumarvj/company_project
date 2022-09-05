from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.models import Employee_view
from.serializer import Emp_serializer

class Employee_model_view_set(ModelViewSet):
    queryset = Employee_view.objects.all()
    serializer_class = Emp_serializer

