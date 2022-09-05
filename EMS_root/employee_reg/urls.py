from django.shortcuts import render
from django.urls import path
from.import views

urlpatterns=[
    path('',views.Home),
    path('contactus/',views.contactus),
    path('aboutus/',views.aboutus),
    path('employee_register/',views.employee_register),
    path('employee_login/',views.employee_login),
    path('employee_logout/',views.employee_logout),
]