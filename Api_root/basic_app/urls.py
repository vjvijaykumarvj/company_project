from django.urls import path,include
from .import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register('basic',views.Basic_auth,basename='basic')


urlpatterns = [
    path('',include(router.urls))
]