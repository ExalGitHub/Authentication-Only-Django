from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('session/', views.login_view, name='session'),
    path('profile/', views.login_view, name='profile'),
]