from django.urls import path
from.import views

urlpatterns=[
    path('new_book/',views.new_book),
    path('new_lobrary/',views.new_lobrary),
    path('home/',views.home),
    path('adminhome/',views.adminhome),
]


