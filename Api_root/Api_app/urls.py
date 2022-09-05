from django.urls import  path
from.import views


urlpatterns=[
    path('Api_cr/',views.Employee_cr.as_view(),name='Api_cr'),
    path('Api_rud/<pk>/',views.Employee_rud.as_view(),name='Api_rud'),
]
