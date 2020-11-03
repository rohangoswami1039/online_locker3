from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home_login',views.login, name='login'),
    path('home_sign_up',views.sign_up, name='sign_up'),
    path('login',views.user_login, name='user_login'),
    path('sign_up',views.user_sign_up, name='user_sign_up'),
]
