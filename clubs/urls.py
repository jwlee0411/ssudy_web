from django.urls import path

from . import views

urlpatterns = [
    path('', views.clubs),
    path('<int:aid>', views.club_list),
    path('info/<int:bid>', views.club_description),
]
