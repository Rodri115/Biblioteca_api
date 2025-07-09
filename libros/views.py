from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Autor, Genero, Libro, Calificacion
from .permissions import IsAdminOrReadOnly
from .serializers import AutorSerializer, GeneroSerializer, LibroSerializer, CalificacionSerializer
from rest_framework import generics
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAdminOrReadOnly]  # Solo admins pueden modificar

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [IsAdminOrReadOnly]  # Solo admins pueden modificar

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAdminOrReadOnly]  # Solo admins pueden modificar

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [IsAuthenticated]  # Cualquier usuario autenticado puede calificar

class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

class LibroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados



class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = []  # permite acceso público (sin autenticación)

class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]