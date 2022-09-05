from django.urls import path
from.import views
app_name= 'kumar'
urlpatterns=[
    path('emp_load/',views.emp_load,name='emp_load'),
    path('emp_create/',views.emp_create,name='emp_create'),
    path('emp_id/<pk>',views.emp_id,name='emp_id'),
    path('emp_update/<pk>',views.emp_update,name='emp_update'),
    path('emp_delete/<pk>',views.emp_delete,name='emp_delete'),
]
