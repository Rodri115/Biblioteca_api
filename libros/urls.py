from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, GeneroViewSet, LibroViewSet, CalificacionViewSet
from .views import UserRegisterAPIView
from .views import RegisterUserAPIView
from rest_framework import viewsets
from .models import Autor, Genero, Libro, Calificacion
from .serializers import AutorSerializer, GeneroSerializer, LibroSerializer, CalificacionSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'calificaciones', CalificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
]
