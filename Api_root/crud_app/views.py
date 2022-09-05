from django.shortcuts import render
from .models import Rooms
from.serializer import roomSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
# Create your views here.

class Crud(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Rooms.objects.all()
    serializer_class = roomSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request)
    def get(self,request,*args,**kwargs):
        return self.list(request)
class Crud_v(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset = Rooms.objects.all()
    serializer_class = roomSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request)
    def put(self,request,*args,**kwargs):
        return self.update(request)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request)






