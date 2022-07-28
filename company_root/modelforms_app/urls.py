from  django.urls import path
from .import views

app_name='employee_form'

urlpatterns=[
    path('employee_dashboard/',views.employee_dashboard),
    path('update_employee/<pk>',views.Update_employee,name='update_employee')
]
