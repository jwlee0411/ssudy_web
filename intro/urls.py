from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('intro1/', views.intro1),
    path('intro2/', views.intro2),
    path('intro3/', views.intro3),
    path('intro4/', views.intro4),
    path('intro5/', views.intro5),
]
