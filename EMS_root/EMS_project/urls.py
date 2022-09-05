from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('employee_reg.urls')),
    path('',include('employee_apply.urls')),
    path('',include('Mixins_app.urls')),
]
