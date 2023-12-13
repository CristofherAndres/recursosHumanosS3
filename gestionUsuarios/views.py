from django.shortcuts import render
from django.http import JsonResponse


#Librerías necesarias API
from .serializers import UsuarioSerializer
from gestionUsuarios.models import Usuario
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404


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

# Consultar persona con su id -> get (id)
# Actualizar la persona el id -> put (id)
# Eliminar la persona el id -> delete (id)

@api_view(['GET','PUT','DELETE'])
def detallesUsuarioAPI(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class listaPersona(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class detallePersona(APIView):
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        persona = self.get_object(pk)
        serializer = UsuarioSerializer(persona)
        return Response(serializer.data)
    
    def put(self, request, pk):
        persona = self.get_object(pk)
        serializer = UsuarioSerializer(persona, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)