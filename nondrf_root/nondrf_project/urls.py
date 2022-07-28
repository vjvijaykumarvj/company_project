from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('employee/',include('CRUD_app.urls')),
    path('employeeCBV/',include('CRUD_app.urls')),
]
