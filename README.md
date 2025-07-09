# 📚 Biblioteca API

Una API RESTful para gestionar libros, autores, géneros y calificaciones. Desarrollada con Django y Django REST Framework, conectada a PostgreSQL, pensada para bibliotecas, clubes de lectura o proyectos educativos.

## 🚀 Tecnologías utilizadas

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- Pillow (para manejo de archivos)
- Postman (para testing de API)
- Git + GitHub

## ⚙️ Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/Rodri115/Biblioteca_api.git
cd Biblioteca_api

# CRear entorno virtual e instalar la dependencias
python -m venv env
env\Scripts\activate  # En Windows
pip install -r requirements.txt


#Configuracion de la base de datos en Settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'biblioteca_db',
        'USER': 'postgres',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


#Ejecutar migraciones y servidor
python manage.py migrate
python manage.py runserver


#Endpoints disponibles

Recurso	Método	Ruta	Descripción
Autores	GET	/api/autores/	Listar autores
Autores	POST	/api/autores/	Crear autor
Libros	GET	/api/libros/	Listar libros
Libros	POST	/api/libros/	Crear libro
Géneros	GET	/api/generos/	Listar géneros
Calificaciones	POST	/api/calificaciones/	Calificar un libro

#Usar con Postman

1- Abrí Postman.
2- Probá rutas como http://127.0.0.1:8000/api/libros/
3- Enviar POST, GET, PUT, DELETE según el caso.
4- Usá form-data para subir archivos como libros PDF.

#Autenticación (Próximamente)
Pronto se implementará autenticación por token o JWT para proteger rutas.

#Estadísticas (Próximamente)
Se agregarán visualizaciones usando pandas y matplotlib.

#Contacto
Si tenés dudas o sugerencias, escribime por GitHub o abrí un Issue.
Hecho con amor por Rodrigo Lugo