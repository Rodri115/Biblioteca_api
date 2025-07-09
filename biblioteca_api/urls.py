from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render
from .views import register 

@login_required
def home(request):
    user = request.user
    html = f"""
    <html>
    <head><title>Biblioteca API</title></head>
    <body style="font-family: Arial; padding: 2rem;">
        <h1>📚 Bienvenido, {user.username}</h1>
        <p>Estas son las opciones disponibles:</p>
        <ul>
            <li><a href="/api/libros/">📘 Libros</a></li>
            <li><a href="/api/autores/">✍️ Autores</a></li>
            <li><a href="/api/generos/">🏷️ Géneros</a></li>
            <li><a href="/api/calificaciones/">⭐ Calificaciones</a></li>
            <li><a href="/logout/">🚪 Cerrar sesión</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/token/', auth_views.LoginView.as_view(template_name='login.html'), name='token_obtain_pair'),
    path('api/token/refresh/', auth_views.LoginView.as_view(template_name='login.html'), name='token_refresh'),
    path('api/', include('libros.urls')),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
