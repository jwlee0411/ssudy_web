from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home),
    path('terms/', views.terms),
    path('privacy/', views.privacy),
    path('ban/', views.ban),
]
