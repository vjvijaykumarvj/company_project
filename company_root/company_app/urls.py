from django.urls import path,include
from . import views

app_name='employee'

urlpatterns=[
    path('',views.load_employee),
    path('create_employee/',views.employee_create),
    path('emp_info/<pk>',views.emp_info,name='emp_info'),
    path('emp_delete/<pk>',views.emp_delete,name='emp_delete'),
    path('emp_update/<pk>',views.emp_update,name='emp_update'),
    path('genericCBV/',views.TestCBV.as_view(),name='genericCBV'),
]
