from django.shortcuts import render
from rest_framework import generics
from .models import Categoria
from .serializers import categoriaserializer

def home(request):
    negocio = {
        'saludo': 'Buenas tardes',
        'pan': 'Hojaldrado',
        'precio': '400$',
        'integral': False,
        'listadepan': ['Hojaldrado','Liso','Queso'],
        'Disponible':{
            'enhorno': False,
            'Disponible': True
        }
    }
    return render(request,'Pagina/index.html',negocio)

class categorialistcreateview(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = categoriaserializer


class categoriadestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = categoriaserializer