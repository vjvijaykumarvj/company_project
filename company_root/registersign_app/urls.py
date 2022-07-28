from  django.urls import path
from .import views

app_name='login_app'

urlpatterns=[
    path('sign_app/',views.sign_app,name='sign_app'),
    path('login/',views.login_details,name='login'),
    path('logout/',views.logout_details,name='logout'),
    path('profilepage/',views.profilepage,name='profilepage'),
]