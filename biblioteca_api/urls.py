from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    html = """
    <html>
    <head><title>Biblioteca API</title></head>
    <body style="font-family: Arial; padding: 2rem;">
        <h1>📚 Bienvenido a la API de la Biblioteca</h1>
        <p>Estas son las opciones disponibles:</p>
        <ul>
            <li><a href="/api/libros/">📘 Libros</a></li>
            <li><a href="/api/autores/">✍️ Autores</a></li>
            <li><a href="/api/generos/">🏷️ Géneros</a></li>
            <li><a href="/api/calificaciones/">⭐ Calificaciones</a></li>
            <li><a href="/admin/">🔐 Panel de administración</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home),  # Página de inicio
    path('admin/', admin.site.urls),
    path('api/', include('libros.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
