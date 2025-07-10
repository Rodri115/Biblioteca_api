from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import AutorViewSet, GeneroViewSet, LibroViewSet, CalificacionViewSet
from .views import UserRegisterAPIView, estadistica_libros_por_genero

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'calificaciones', CalificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('estadisticas/libros-por-genero/', estadistica_libros_por_genero, name='libros-por-genero'),
]
