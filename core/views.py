from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from crud.models import Producto


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")

def playstation(request):
    context = {'productos':Producto.objects.filter(marca=1)}
    return render(request, "core/playstation.html",context)

def nintendo(request):
    context = {'productos':Producto.objects.filter(marca=3)}
    return render(request, "core/nintendo.html",context)

def microsoft(request):
    context = {'productos':Producto.objects.filter(marca=2)}
    return render(request, "core/microsoft.html",context)

def figuras(request):
    context = {'productos':Producto.objects.filter(marca=4)}
    return render(request, "core/figuras.html",context)

def accesorios(request):
    context = {'productos':Producto.objects.filter(marca=5)}
    return render(request, "core/accesorios.html",context)

def login(request):
    return render(request, "core/login.html")

def register(request):        
    return render(request, "core/register.html")

def forgot(request):
    return render(request, "core/forgot.html")

def error(request):
    return render(request, "core/404.html")