from django.urls import path
from . import views

urlpatterns=[

    #Function Based View
    #http://127.0.0.1:8000/employee/employee_cr/
    path('employee_cr/',views.Employee_cr),
    #http://127.0.0.1:8000/employee/employee_rud/1
    path('employee_rud/<pk>',views.Employee_rud,name='employee_rud'),

    #Class Based View
    #http://127.0.0.1:8000/employeeCBV/employeeCBV_cr/
    path('employeeCBV_cr/',views.Employee_CR.as_view(),name='employeeCBV_cr'),
    #http://127.0.0.1:8000/employeeCBV/employeeCBV_rud/
    path('employeeCBV_rud/<pk>',views.Employee_RUD.as_view(),name='employeeCBV_rud'),

]