import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import platform
from collections import Counter

# Ruta al CSV (al nivel de manage.py)
csv_path = os.path.join(os.path.dirname(__file__), '..', 'datos_libros.csv')
df = pd.read_csv(csv_path)

# Parsear fechas de lanzamiento (original intacta en 'fecha_lanzamiento')
df['fecha_lanzamiento_parseada'] = pd.to_datetime(
    df['fecha_lanzamiento'], errors='coerce'
)

with PdfPages("reporte_analisis_completo.pdf") as pdf:
    # 1. Cantidad de libros por género
    genero_counts = df['genero'].value_counts()
    genero_counts.plot(kind='bar', title='Cantidad de libros por género', color='skyblue')
    plt.xlabel('Género'); plt.ylabel('Cantidad de libros')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 2. Promedio de calificación por género
    promedios = df.groupby('genero')['calificacion_promedio'].mean()
    promedios.plot(kind='barh', title='Promedio de calificación por género', color='green')
    plt.xlabel('Promedio de calificación')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 3. Distribución por nacionalidad del autor
    df['nacionalidad_autor'].value_counts().plot(
        kind='pie', autopct='%1.1f%%', title='Distribución por nacionalidad del autor'
    )
    plt.ylabel('')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 4. Top 5 autores con más libros
    top_autores = df['autor'].value_counts().head(5)
    top_autores.plot(kind='bar', title='Top 5 autores con más libros', color='orange')
    plt.xlabel('Autor'); plt.ylabel('Cantidad de libros')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 5. Cantidad de libros por década
    df['decada'] = (df['fecha_lanzamiento_parseada'].dt.year // 10) * 10
    df['decada'] = df['decada'].fillna('Desconocida')
    df['decada'].value_counts().sort_index().plot(
        kind='line', marker='o', title='Cantidad de libros por década'
    )
    plt.xlabel('Década'); plt.ylabel('Cantidad de libros')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 6. Distribución de calificaciones
    df['calificacion_promedio'].round().value_counts().sort_index().plot(
        kind='pie', autopct='%1.1f%%', title='Distribución de calificaciones'
    )
    plt.ylabel('')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 7. Histograma de años de lanzamiento
    years = df['fecha_lanzamiento_parseada'].dt.year.dropna()
    plt.hist(years, bins=range(int(years.min()), int(years.max())+2), edgecolor='black')
    plt.title('Histograma de años de lanzamiento')
    plt.xlabel('Año'); plt.ylabel('Cantidad de libros')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 8. Boxplot de calificaciones promedio
    plt.boxplot(df['calificacion_promedio'].dropna())
    plt.title('Boxplot de calificaciones promedio')
    plt.ylabel('Calificación promedio')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # 9. Top 20 palabras en títulos de libros
    all_words = Counter()
    for title in df['nombre'].dropna():
        words = [w.strip('.,;:!?"()').lower() for w in title.split()]
        all_words.update(words)
    top_words = dict(all_words.most_common(20))
    pd.Series(top_words).plot(
        kind='bar', title='Top 20 palabras en títulos', color='purple'
    )
    plt.xlabel('Palabra'); plt.ylabel('Frecuencia')
    plt.tight_layout()
    pdf.savefig(); plt.close()

# Abrir automáticamente el PDF
if platform.system() == "Windows":
    os.startfile("reporte_analisis_completo.pdf")
elif platform.system() == "Darwin":
    os.system("open reporte_analisis_completo.pdf")
else:
    os.system("xdg-open reporte_analisis_completo.pdf")
