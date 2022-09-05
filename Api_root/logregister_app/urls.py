from django.urls import path
from.import views


urlpatterns=[
    path('register/',views.Register),
    path('user_login/',views.user_login),
    path('profile/',views.profile),
    path('user_logout/',views.user_logout),
    # path('img/',views.Img),
]
