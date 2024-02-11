from django.urls import path
from . import views

app_name = "class"
urlpatterns = [
    path('create/', views.create),
    path('confirm/<int:id>', views.confirm),
    path('delete/<int:id>', views.delete),
    path('', views.check),
    path('result/<int:id>-<str:checksum>', views.check_result),
    path('result/<str:checksum>', views.check_result_2),
    path('result/', views.check_result_3),
    path('print/<int:id>-<str:checksum>', views.class_print),
    path('read/<int:id>', views.read),
    path('list/', views.list2),
]