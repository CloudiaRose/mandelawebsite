# mandela/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('home/', views.home, name='home'),
    path('biography/', views.biography, name='biography'),
    path('quotes/', views.quotes, name='quotes'),
    path('legacy/', views.legacy, name='legacy'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
]
