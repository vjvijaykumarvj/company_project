from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_app.urls')),
    path('', include('model_view_app.urls')),
    path('', include('model_view_set_app.urls')),
    path('', include('base_token_app.urls')),
    path('', include('Api_app.urls')),
    path('get_api_token',views.obtain_auth_token,name='get_api_token'),
    path('',include('logregister_app.urls')),
    path('',include('new_app.urls')),
    path('',include('basic_app.urls')),

]
