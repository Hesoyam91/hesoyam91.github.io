from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contacto/', views.contacto, name="contacto"),
    path('playstation/', views.playstation, name="playstation"),
    path('nintendo/', views.nintendo, name="nintendo"),
    path('microsoft/', views.microsoft, name="microsoft"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('forgot/', views.forgot, name="forgot"),
    path('404/', views.error, name="404"),
    path('figuras/', views.figuras, name="figuras"),
    path('accesorios/', views.accesorios, name="accesorios"),
    
]