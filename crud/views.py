from email.mime import image
from logging.config import stopListening
from math import prod
import re
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from .forms import ProductoForm
from .models import *

# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/product_list.html',context)

def product_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Producto.objects.create(
                idProducto = idProducto,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imagen,
                marca = marca
            )
            obj.save()
            return redirect(reverse('product-list') + "?OK")
        else:
            return redirect(reverse('product-list') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/product_new.html',{'form':form})

def product_detail(request,product_id):    
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/product_detail.html',context)
    except:
        return redirect(reverse('product-list'))

def product_update(request,product_id):
    producto = Producto.objects.get(idProducto=product_id)
    if producto:
        form = ProductoForm(instance=producto)
    else:
        return redirect(reverse('product-list') + "?FAIL")

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance = producto)
        if form.is_valid():
            form.save()
            return redirect(reverse('product-list') + "?OK")
        else:
                return redirect(reverse('product-update') + product_id)
    
    return render(request,'crud/product_update.html',{'form':form})

def product_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto = product_id)
        producto.delete()
        return redirect(to = 'product-list')
    except:
        return redirect(reverse('product-list') + "?FAIL")

