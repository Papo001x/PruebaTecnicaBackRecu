# 🐍 Backend - API GraphQL con Django + MySQL

Este es el backend del sistema de estadísticas de ventas, construido con **Django** y **Graphene-Django** para exponer una **API GraphQL**. Usa **MySQL** como base de datos principal.

---

## 🚀 Requisitos

- Python 3.10+
- MySQL Server
- pipenv o virtualenv
- Un entorno MySQL configurado

---

## ⚙️ Configuración inicial

1. **Clona el repositorio y accede a la carpeta del backend**:

```bash
git clone https://github.com/tu-usuario/tu-repo-backend.git
cd tu-repo-backend
```

2. **Crea entorno virtual e instala dependencias**:

```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configura la conexión a la base de datos MySQL** en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ventas_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🛠 Migraciones e inicialización

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧪 Crear datos de prueba

Puedes usar el admin de Django para insertar productos, clientes y ventas:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Accede a: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🚀 Ejecutar servidor

```bash
python manage.py runserver
```

La API GraphQL estará disponible en:

```
http://localhost:8000/graphql
```

---

## 📁 Estructura

```
ventas/
├── models.py        # Modelos: Product, Customer, Sale
├── schema.py        # Esquema GraphQL (graphene)
├── views.py         # No se usa (GraphQL gestiona todo)
├── admin.py         # Registro de modelos
└── ...
```

---

## ✅ Funcionalidades

- API GraphQL para consultar:
  - Ventas totales por mes
  - Ventas totales por producto
  - Lista de productos, clientes y ventas
- Compatible con Apollo Client (frontend)
- Base de datos MySQL

---

## 🧩 Notas adicionales

- Asegúrate de que el servidor MySQL esté activo
- Verifica que los datos existen antes de hacer queries
- Habilita CORS si el frontend está en otro puerto

---

## 🧑‍💻 Autor

Desarrollado por **Brandon** como parte de una prueba técnica.

