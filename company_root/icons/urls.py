from django.urls import path
from . import views

urlpatterns=[
    path('icons/',views.icons),
    path('student/',views.student),
]

