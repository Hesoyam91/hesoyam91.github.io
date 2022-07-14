from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contacto/', views.contacto, name="contacto"),
    path('productos_ps4/', views.productos_ps4, name="ps4"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('forgot/', views.forgot, name="forgot"),
    
]