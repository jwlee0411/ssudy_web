from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main),
    path('popup/', views.popup),
    path('front/', views.front),
    path('email/', views.email),
    path('email_all/', views.email_all),
    path('terms/', views.terms),
    # path('board/', views.board),
    path('main_board/', views.main_board),
    path('delete_club/', views.delete_club),
    path('class_setting/', views.class_setting),
    path('class_add/', views.class_add),
    path('class_delete/', views.class_delete),
    path('class_delete/<int:bid>', views.class_delete_final),
    path('delete_club/delete/<int:bid>', views.delete),
    path('intro/', views.clubs),
    path('maintenance/', views.maintenance),

]
