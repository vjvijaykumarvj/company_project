from django.urls import path
from.import views

urlpatterns = [
    path('Crud/',views.Crud.as_view(),name='Crud'),
    path('Crud/<pk>/',views.Crud_v.as_view(),name='Crud'),
]
