import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os 
import django
from django.db.models import Avg
from .models import Libro

os.environ.setdefault("DJANGO_SETTING_MODULE", "biblioteca_api.settings")
django.setup()

def libros_por_genero_chart():
    # Consultar libros con su género
    qs = Libro.objects.select_related("genero")\
        .values("genero__nombre")\
        .annotate(cantidad=pd.NamedAgg(column='id', aggfunc='count'))

    # Convertir a DataFrame
    df = pd.DataFrame(list(qs))
    if df.empty:
        return None  # No hay datos

    # Crear gráficoimport os
import django
import pandas as pd
import matplotlib.pyplot as plt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca_api.settings")
django.setup()

from libros.models import Libro

def promedio_por_genero():
    data = Libro.objects.select_related("genero").prefetch_related("calificaciones").values(
        "genero__nombre", "calificaciones__valor"
    )
    df = pd.DataFrame(data)
    promedio = df.groupby("genero__nombre")["calificaciones__valor"].mean().sort_values(ascending=False)
    promedio.plot(kind="bar", title="Promedio por género")
    plt.tight_layout()
    plt.savefig("promedio_por_genero.png")
    plt.close()

def promedio_por_autor():
    data = Libro.objects.select_related("autor").prefetch_related("calificaciones").values(
        "autor__nombre", "calificaciones__valor"
    )
    df = pd.DataFrame(data)
    promedio = df.groupby("autor__nombre")["calificaciones__valor"].mean().sort_values(ascending=False).head(10)
    promedio.plot(kind="bar", title="Top 10 autores mejor calificados")
    plt.tight_layout()
    plt.savefig("top10_autores.png")
    plt.close()

def promedio_por_nacionalidad():
    data = Libro.objects.select_related("autor").prefetch_related("calificaciones").values(
        "autor__nacionalidad", "calificaciones__valor"
    )
    df = pd.DataFrame(data)
    promedio = df.groupby("autor__nacionalidad")["calificaciones__valor"].mean().sort_values(ascending=False)
    promedio.plot(kind="bar", title="Promedio por nacionalidad")
    plt.tight_layout()
    plt.savefig("promedio_nacionalidad.png")
    plt.close()

def libros_por_decada():
    data = Libro.objects.values("fecha_lanzamiento")
    df = pd.DataFrame(data)
    df["anio"] = pd.to_datetime(df["fecha_lanzamiento"], errors="coerce").dt.year
    df["decada"] = (df["anio"] // 10) * 10
    conteo = df["decada"].value_counts().sort_index()
    conteo.plot(kind="bar", title="Libros por década")
    plt.tight_layout()
    plt.savefig("libros_por_decada.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(df['genero__nombre'], df['cantidad'], color='skyblue')
    plt.title('Cantidad de Libros por Género')
    plt.xlabel('Género')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar gráfico en memoria
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Codificar en base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic
