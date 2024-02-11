from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'common'
urlpatterns = [
    path('mypage/', views.mypage),
    path('mypage1/', views.mypage1),
    path('mypage2/', views.mypage2),
    path('mypage3/', views.mypage3),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_terms/', views.signup_terms),
    path('signup2/<str:username>', views.signup2),
    ]