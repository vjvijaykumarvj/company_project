from django.urls import path
from.import views

urlpatterns=[
    path('mixin_list/',views.mixin_list.as_view(),name='mixin_list'),
    path('mixin_create/',views.mixin_create.as_view(),name='mixin_create'),
    path('mixin_l/<pk>',views.mixin_l.as_view(),name='mixin_l'),
    path('mixin_up/<pk>',views.mixin_up.as_view(),name='mixin_up'),
]