import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca_api.settings")
django.setup()

from libros.models import Libro

def recomendar_libros():
    genero = input("📚 Ingrese un género: ")
    data = Libro.objects.select_related("genero").prefetch_related("calificaciones").filter(
        genero__nombre=genero
    ).values("nombre", "calificaciones__valor")
    df = pd.DataFrame(data)
    if df.empty:
        print("❌ No se encontraron libros.")
        return
    df = df.sort_values(by="calificaciones__valor", ascending=False)
    print(f"\n✅ Libros recomendados para el género '{genero}':\n")
    for _, row in df.iterrows():
        print(f"→ {row['nombre']} (Calificación: {row['calificaciones__valor']})")

if __name__ == "__main__":
    recomendar_libros()
