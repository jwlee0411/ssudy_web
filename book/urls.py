from django.urls import path

from . import views

urlpatterns = [


    path('read_new/<int:bid>', views.read_new),

    path('cancel_new/<int:aid>', views.cancel_new),
    path('confirm_new/<int:aid>', views.confirm_new),
    path('create_new/', views.create_new_main),
    path('create_new/<str:room>', views.create_new),
    path('create_new/<str:room>/', views.create_new_error),
    path('create_new/<str:room>/<str:date>', views.create_new2),
    path('create_new/<str:room>/<str:date>/<int:time>', views.create_new3),


    path('create_new_admin/', views.create_new_admin),



    path('list_new/', views.list_new),
    path('list_new/<str:date>', views.list_new2),
    path('list_new/room/<str:room>', views.list_new3),
    path('list_admin/', views.list_new_admin),
    path('list_admin/<str:date>', views.list_new_admin2),

]
