from rest_framework import serializers
from crud.models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'idProducto','descripcion','precio','stock','marca'
        )

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = (
            'id','marca'
        )