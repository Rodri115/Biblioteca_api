# 📚 Biblioteca API

Una API RESTful robusta para gestionar libros, autores, géneros y calificaciones. Desarrollada con Django y Django REST Framework, conectada a PostgreSQL, perfecta para bibliotecas, clubes de lectura o proyectos educativos.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-Latest-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Características

- **Gestión completa de libros**: CRUD completo para libros con soporte para archivos PDF
- **Administración de autores**: Gestión de información detallada de autores
- **Categorización por géneros**: Organización eficiente mediante géneros literarios
- **Sistema de calificaciones**: Permite a los usuarios calificar y reseñar libros
- **API RESTful**: Endpoints bien documentados siguiendo las mejores prácticas
- **Base de datos PostgreSQL**: Almacenamiento robusto y escalable
- **Subida de archivos**: Soporte para archivos PDF de libros

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.12, Django 5.2
- **API Framework**: Django REST Framework
- **Base de Datos**: PostgreSQL
- **Manejo de Archivos**: Pillow
- **Testing**: Postman
- **Control de Versiones**: Git + GitHub

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.12 o superior
- PostgreSQL
- pip (gestor de paquetes de Python)
- Git

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Rodri115/Biblioteca_api.git
cd Biblioteca_api
```

### 2. Crear y activar entorno virtual

```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual
# En Windows
env\Scripts\activate

# En macOS/Linux
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Crea una base de datos PostgreSQL y configura las credenciales en `settings.py`:

```python
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
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`

## 📡 API Endpoints

### Autores

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/autores/` | Listar todos los autores |
| `POST` | `/api/autores/` | Crear nuevo autor |
| `GET` | `/api/autores/{id}/` | Obtener autor específico |
| `PUT` | `/api/autores/{id}/` | Actualizar autor |
| `DELETE` | `/api/autores/{id}/` | Eliminar autor |

### Libros

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/libros/` | Listar todos los libros |
| `POST` | `/api/libros/` | Crear nuevo libro |
| `GET` | `/api/libros/{id}/` | Obtener libro específico |
| `PUT` | `/api/libros/{id}/` | Actualizar libro |
| `DELETE` | `/api/libros/{id}/` | Eliminar libro |

### Géneros

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/generos/` | Listar todos los géneros |
| `POST` | `/api/generos/` | Crear nuevo género |
| `GET` | `/api/generos/{id}/` | Obtener género específico |
| `PUT` | `/api/generos/{id}/` | Actualizar género |
| `DELETE` | `/api/generos/{id}/` | Eliminar género |

### Calificaciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/calificaciones/` | Crear nueva calificación |
| `GET` | `/api/calificaciones/` | Listar calificaciones |

## 🧪 Pruebas con Postman

1. **Instalar Postman** desde [postman.com](https://www.postman.com/)
2. **Importar colección** (si está disponible) o crear requests manualmente
3. **Configurar base URL**: `http://127.0.0.1:8000`
4. **Probar endpoints**:
   - GET `http://127.0.0.1:8000/api/libros/`
   - POST `http://127.0.0.1:8000/api/autores/`
   - Para subir archivos, usar `form-data` en el body

### Ejemplo de uso con cURL

```bash
# Listar libros
curl -X GET http://127.0.0.1:8000/api/libros/

# Crear nuevo autor
curl -X POST http://127.0.0.1:8000/api/autores/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Gabriel García Márquez", "nacionalidad": "Colombiano"}'
```

## 📊 Estructura del Proyecto

```
Biblioteca_api/
├── biblioteca_api/        # Configuración principal del proyecto
│   ├── settings.py       # Configuraciones de Django
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # Configuración WSGI
├── apps/                 # Aplicaciones Django
│   ├── libros/          # App de libros
├── media/               # Archivos subidos
├── static/              # Archivos estáticos
├── requirements.txt     # Dependencias del proyecto
├── manage.py           # Script de gestión de Django
│── analisis/             # Aplicaciones Django
│   ├── analisis.py/   # Analisis de datos
└── README.md           # Este archivo
```

## 🔮 Próximas Características

- **Autenticación y Autorización**: Implementación de JWT o autenticación por token
- **Estadísticas y Análisis**: Visualizaciones con pandas y matplotlib
- **Búsqueda Avanzada**: Filtros y búsqueda por múltiples criterios
- **Sistema de Recomendaciones**: Algoritmos de recomendación basados en calificaciones
- **Documentación OpenAPI**: Swagger/OpenAPI para documentación interactiva
- **Tests Automatizados**: Suite completa de pruebas unitarias e integración

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📧 Contacto

**Rodrigo Lugo**
- GitHub: [@Rodri115](https://github.com/Rodri115)
- Email: [tu-email@ejemplo.com]

---

## 🙏 Agradecimientos

- Django y Django REST Framework por las herramientas excepcionales
- La comunidad de desarrolladores por las mejores prácticas
- Todos los contribuidores que hacen este proyecto posible

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella!

**Hecho con ❤️ por Rodrigo Lugo**