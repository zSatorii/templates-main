from rest_framework import serializers
from .models import Categoria

class categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'cantidad']
