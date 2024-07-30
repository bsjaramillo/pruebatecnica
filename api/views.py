from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    @action(detail=True, methods=['get'])
    def find_by_autor(self, request, pk=None):
        libros = Libro.objects.filter(autor=pk)
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def find_by_category(self, request, pk=None):
        libros = Libro.objects.filter(categoria=pk)
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def find_by_editorial(self, request, pk=None):
        libros = Libro.objects.filter(editorial=pk)
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=['get'])
    def find_by_category(self, request, pk=None):
        libros = Libro.objects.filter(categoria=pk)
        autores = [libro.autor for libro in libros]
        serializer = AutorSerializer(autores, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
