from django.contrib import admin
from .models import Autor, Genero, Libro, Calificacion

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
    list_per_page = 10

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 10

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_lanzamiento', 'genero', 'autor', 'book_url')
    list_filter = ('genero', 'autor')
    search_fields = ('nombre', 'autor__nombre')
    list_per_page = 10

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro', 'valor')
    list_filter = ('valor',)
    search_fields = ('libro__nombre',)
    list_per_page = 10