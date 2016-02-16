from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from usuario.models import Usuario
from api.serializers import UsuarioSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def usuario_list(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )



@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, name, password):
    try:
        usuario = Usuario.objects.get(name=name, password=password)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #except Usuario.MultipleObjectsReturned:
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status_HTTP_400_BAD_REQUEST
            )

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
