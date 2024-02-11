from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('create/', views.create),
    path('modify/<int:bid>', views.modify),
    path('list/<int:aid>', views.list2), # 공지사항
    path('read/<int:bid>', views.read),
    path('search/<str:name>', views.search),
    path('download/<str:file_name>', views.file_download),
    path('delete/<int:bid>', views.delete),

]