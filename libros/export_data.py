# libros/export_data.py
import pandas as pd
from .models import Libro, Autor, Genero, Calificacion

def export_data():
    libros = Libro.objects.select_related('autor', 'genero').all()
    data = []

    for libro in libros:
        calificaciones = libro.calificaciones.values_list('valor', flat=True)
        promedio_calificacion = sum(calificaciones) / len(calificaciones) if calificaciones else None

        data.append({
            'id': libro.id,
            'nombre': libro.nombre,
            'fecha_lanzamiento': libro.fecha_lanzamiento,
            'genero': libro.genero.nombre if libro.genero else None,
            'autor': libro.autor.nombre,
            'nacionalidad_autor': libro.autor.nacionalidad,
            'calificacion_promedio': promedio_calificacion,
        })

    df = pd.DataFrame(data)
    df.to_csv("datos_libros.csv", index=False)
    return df
