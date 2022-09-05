from django.urls import path, include
from.import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('employee',views.Employee_crud,basename='employee')

urlpatterns=[
    path('',include(router.urls))
]
