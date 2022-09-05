from django.urls import path, include
from rest_framework import routers
from.import views


router = routers.SimpleRouter()
router.register('token_base',views.Token_base,basename='token_base')


urlpatterns=[
    path('',include(router.urls))
]