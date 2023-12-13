from django.shortcuts import render
from django.http import JsonResponse


#Librerías necesarias API
from .serializers import UsuarioSerializer
from gestionUsuarios.models import Usuario
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

def vistaUsuario(request):
    usuario = {
        'id': 123456,
        'nombre': 'Juan',
        'email': 'juan@talca.cl',
        'sueldo': 5000
    }
    return JsonResponse(usuario)

def vistaUsuario2(request):
    #Obtener todos los datos
    usuarios = Usuario.objects.all()
    data = {
        'usuarios': list(usuarios.values('nombre','sueldo'))
    }
    return JsonResponse(data)

@api_view(['GET','POST'])
#GET obtener todos los datos
#POST insertar datos mediante un json
def vistaUsuarioApi(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)