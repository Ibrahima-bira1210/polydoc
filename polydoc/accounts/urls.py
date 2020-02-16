from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/',views.user_login , name = 'user_login'),
    path('logout/',views.logout, name = 'user_logout'),
    path('register/', views.register,name='register'),
    path('profil/',views.profile,name = 'profile'),
]
