from django.urls import path
from.import views
app_name = 'vijay'

urlpatterns=[
    path('emp_dashboard/',views.emp_dashboard),
    path('emp_update/<pk>',views.emp_update,name='emp_update'),
    path('emp_delete/<pk>',views.emp_delete,name='emp_delete'),
]