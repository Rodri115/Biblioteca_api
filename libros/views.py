from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Autor, Genero, Libro, Calificacion
from .permissions import IsAdminOrReadOnly
from .serializers import AutorSerializer, GeneroSerializer, LibroSerializer, CalificacionSerializer, UserRegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import logout
from django.http import JsonResponse
from .analytics import libros_por_genero_chart

# --- CRUD de modelos principales ---
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAdminOrReadOnly]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [IsAdminOrReadOnly]

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAdminOrReadOnly]

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [IsAuthenticated]

# --- Registro de usuarios ---
class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

# --- Estadísticas (gráfico libros por género) ---
def estadistica_libros_por_genero(request):
    chart = libros_por_genero_chart()
    if chart:
        return JsonResponse({'grafico_base64': chart})
    return JsonResponse({'mensaje': 'No hay datos'}, status=404)

# --- Login que devuelve el token ---
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })

# --- Logout (elimina el token del usuario) ---
from rest_framework.views import APIView
from rest_framework import status

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # elimina el token
        logout(request)
        return Response({'mensaje': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
