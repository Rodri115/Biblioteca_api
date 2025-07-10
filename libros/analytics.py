import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from django.db.models import Avg
from .models import Libro

def libros_por_genero_chart():
    # Consultar libros con su género
    qs = Libro.objects.select_related("genero")\
        .values("genero__nombre")\
        .annotate(cantidad=pd.NamedAgg(column='id', aggfunc='count'))

    # Convertir a DataFrame
    df = pd.DataFrame(list(qs))
    if df.empty:
        return None  # No hay datos

    # Crear gráfico
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
