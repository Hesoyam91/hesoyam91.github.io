from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")

def productos_ps4(request):
    return render(request, "core/productos_ps4.html")

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")

def forgot(request):
    return render(request, "core/forgot.html")