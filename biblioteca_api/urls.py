from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token
from .views import register, home  # Import from main project views
from django.contrib import admin
from django.urls import path, include
from libros.views import login_view, logout_view, register, home


@login_required
def home_placeholder(request):
    # This is just a placeholder since you have your own home view
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
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('api/', include('libros.urls')),  # tus endpoints API
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)