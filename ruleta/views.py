import numpy as np
from django.http import JsonResponse
from django.shortcuts import render

def ruleta_page(request):
    return render(request, 'ruleta/ruleta.html')

def ruleta_casino(request):
    numeros = np.arange(37)
    colores = ['verde' if i == 0 else 'rojo' if i % 2 == 1 else 'negro' for i in numeros]
    resultado = np.random.choice(numeros)
    color_resultado = colores[resultado]

    datos = {
        'numero': int(resultado),
        'color': color_resultado,
    }
    return JsonResponse(datos)
