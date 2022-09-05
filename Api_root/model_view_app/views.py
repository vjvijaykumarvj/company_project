from django.shortcuts import render
from rest_framework import response
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from.models import Employee_view
from.serializer import Emp_serializer

class Employee_crud(ViewSet):
    def create(self,request,*args,**kwargs):
        # get the employee from clinet
        emp_json = request.data
        emp_serializer = Emp_serializer(data=emp_json)
        if emp_serializer.is_valid():
            emp_serializer.save()
        return Response(emp_serializer.data)
    def list(self,request,*args,**kwargs):
        # get the all employee from database
        employee_qs = Employee_view.objects.all()
        serializer = Emp_serializer(employee_qs,many=True)
        emp_dict = serializer.data
        return Response(emp_dict)
    def retrieve(self,request,pk,*args,**kwargs):
        # get the single employee record from database
        emp_object= Employee_view.objects.get(id=pk)
        emp_serializer = Emp_serializer(emp_object,many=False)
        # emp_dict = emp_serializer.data  # this one also applicable
        return Response(emp_serializer.data)
    def update(self,request,pk,*args,**kwargs):
        # get the data from client
        emp_json = request.data
        emp_object = Employee_view.objects.get(id=pk)
        emp_serializer = Emp_serializer(instance=emp_object,data=emp_json)
        if emp_serializer.is_valid():
            emp_serializer.save()
        return Response(emp_serializer.data)
    def delete(self,request,pk,*args,**kwargs):
        emp_data = Employee_view.objects.get(id=pk)
        emp_data.delete()
        return Response({'msg':'delete Employee data successfully'})






