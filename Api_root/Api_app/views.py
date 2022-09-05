from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Employee_model
from .seralizer import Emp_serializer
from django.shortcuts import HttpResponse

class Employee_cr(APIView):
    def post(self,request,*args,**kwargs):
        # get the employee from client
        emp_json = request.body
        # convert json to dict
        stream = io.BytesIO(emp_json)
        emp_dict = JSONParser().parse(stream)
        #serailiser pass emp_dict to serializer
        emp_serializer = Emp_serializer(data=emp_dict)
        if emp_serializer.is_valid():
            emp_serializer.save()
        #pasing the messege the output
        emp_msg = {'msg':'create employee successfully'}
        msg_json = JSONRenderer().render(emp_msg)
        return HttpResponse(msg_json,content_type='application/json')
    def get(self,request,*args,**kwargs):
        # get the all employee from database
        emp_data = Employee_model.objects.all()
        emp_serialiser = Emp_serializer(emp_data,many=True)
        emp_dict = emp_serialiser.data
        emp_json = JSONRenderer().render(emp_dict)
        return HttpResponse(emp_json,content_type='application/json')
class Employee_rud(APIView):
    def get(self,request,pk,*args,**kwargs):
        # get the singe employee data from database
        emp_data = Employee_model.objects.get(id=pk)
        emp_serializer = Emp_serializer(emp_data,many=False)
        emp_dict = emp_serializer.data
        emp_json = JSONRenderer().render(emp_dict)
        return HttpResponse(emp_json,content_type='application/json')
    def put(self,request,pk,*args,**kwargs):
        # get the employee from client
        emp_json = request.body
        stream= io.BytesIO(emp_json)
        emp_dict = JSONParser().parse(stream)
        # get the employee from database and that one update
        emp_qs = Employee_model.objects.get(id=pk)
        # serailazer class can applly qs object to normal data comes purpose
        emp_serilizer = Emp_serializer(emp_qs,emp_dict)
        if emp_serilizer.is_valid():
            emp_serilizer.save()
        ret_msg = {'msg':'employee update successfully'}
        msg_json = JSONRenderer().render(ret_msg)
        return HttpResponse(msg_json,content_type='application/json')
    def delete(self,request,pk,*args,**kwargs):
        # get the data from database and that one delete
        emp_qs  =Employee_model.objects.get(id=pk)
        emp_qs.delete()
        res_msg = {'msg':'delete employee successfully'}
        ret_json = JSONRenderer().render(res_msg)
        return HttpResponse(ret_json,content_type='application/json')


