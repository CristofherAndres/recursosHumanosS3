from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def vistaUsuario(request):
    usuario = {
        'id': 123456,
        'nombre': 'Juan',
        'email': 'juan@talca.cl',
        'sueldo': 5000
    }

    return JsonResponse(usuario)