from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from.models import Employee
from.serializer import Employee_serializer
# Create your views here.

class mixin_list(GenericAPIView,ListModelMixin):
    serializer_class = Employee_serializer
    queryset = Employee.objects.all()
    def get(self,request):
        return self.list(request)
class mixin_create(GenericAPIView,CreateModelMixin):
    serializer_class = Employee_serializer
    queryset = Employee.objects.all()
    def post(self,request):
        return self.create(request)
class mixin_l(GenericAPIView,RetrieveModelMixin):
    serializer_class = Employee_serializer
    queryset = Employee.objects.all()
    def get(self, request,pk ,*args, **kwargs):
        return self.retrieve(request,pk)
class mixin_up(GenericAPIView,UpdateModelMixin):
    serializer_class = Employee_serializer
    queryset = Employee.objects.all()
    def put(self, request,pk,*args,**kwargs):
        return self.update(request,pk)


