from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, related_name='libros')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    book_url = models.FileField(upload_to='libros/')

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    OPCIONES_CALIFICACION = [
        (1, 'Bueno'),
        (2, 'Muy Bueno'),
        (3, 'Malo'),
        (4, 'Muy Malo'),
    ]

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='calificaciones')
    valor = models.IntegerField(choices=OPCIONES_CALIFICACION)

    def __str__(self):
        return f"{self.get_valor_display()} - {self.libro.nombre}"
