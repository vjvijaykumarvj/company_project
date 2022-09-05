from rest_framework import routers
from django.urls import path, include
from.import views

router = routers.SimpleRouter()
router.register('model_view_set',views.Employee_model_view_set,basename='model_view_set')

urlpatterns=[
    path('',include(router.urls))
]