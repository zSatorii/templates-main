from django.shortcuts import render, redirect
from .models import Contacto

def summit_home(request):
    if request.method == 'POST':
        Contacto.objects.create(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            asunto=request.POST.get('asunto'),
            mensaje=request.POST.get('mensaje'),
        )
        return redirect('summit_home') 
    return render(request, 'summit/index.html')
