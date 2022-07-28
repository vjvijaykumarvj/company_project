from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('item/',include('icons.urls')),
    path('contactus/',views.contactus),
    path('aboutus/',views.aboutus),
    path('studenthp/',include('icons.urls')),
    path('dtl/',views.dtl),
    path('employee/',include('company_app.urls')),
    path('login_app/',include('registersign_app.urls')),
    path('employee_form/',include('modelforms_app.urls')),
]
