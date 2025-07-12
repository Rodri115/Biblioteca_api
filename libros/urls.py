from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    AutorViewSet, GeneroViewSet, LibroViewSet, CalificacionViewSet,
    UserRegisterAPIView, estadistica_libros_por_genero,
    acceso_denegado, vista_crud_libros,
    libro_list, libro_create, libro_update, libro_delete,
    autor_list, autor_create, autor_update, autor_delete,
    genero_list, genero_create, genero_update, genero_delete,
    calificacion_list, calificacion_create, calificacion_update, calificacion_delete,
)

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'calificaciones', CalificacionViewSet)

urlpatterns = [
    # API
    path('', include(router.urls)),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('estadisticas/libros-por-genero/', estadistica_libros_por_genero, name='libros-por-genero'),
    path('acceso-denegado/', acceso_denegado, name='acceso_denegado'),
    path('admin/libros/', vista_crud_libros, name='crud_libros'),

    # Web: CRUD Libros
    path('web/libros/', libro_list, name='libro_list'),
    path('web/libros/nuevo/', libro_create, name='libro_create'),
    path('web/libros/editar/<int:pk>/', libro_update, name='libro_update'),
    path('web/libros/eliminar/<int:pk>/', libro_delete, name='libro_delete'),

    # Web: CRUD Autores
    path('web/autores/', autor_list, name='autor_list'),
    path('web/autores/nuevo/', autor_create, name='autor_create'),
    path('web/autores/editar/<int:pk>/', autor_update, name='autor_update'),
    path('web/autores/eliminar/<int:pk>/', autor_delete, name='autor_delete'),

    # Web: CRUD Géneros
    path('web/generos/', genero_list, name='genero_list'),
    path('web/generos/nuevo/', genero_create, name='genero_create'),
    path('web/generos/editar/<int:pk>/', genero_update, name='genero_update'),
    path('web/generos/eliminar/<int:pk>/', genero_delete, name='genero_delete'),

    # Web: CRUD Calificaciones
    path('web/calificaciones/', calificacion_list, name='calificacion_list'),
    path('web/calificaciones/nuevo/', calificacion_create, name='calificacion_create'),
    path('web/calificaciones/editar/<int:pk>/', calificacion_update, name='calificacion_update'),
    path('web/calificaciones/eliminar/<int:pk>/', calificacion_delete, name='calificacion_delete'),
]
