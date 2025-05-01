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

2. **Instala dependencias**:

```bash
pip install -r requirements.txt
```

3. **Configura la conexión a la base de datos MySQL** en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ventas',
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

Ejecuta el SQL de datos prueba dentro de la base de datos llamada ventas.


## 🚀 Ejecutar servidor

```bash
python manage.py runserver
```

La API GraphQL estará disponible en:

```
http://localhost:8000/graphql
```

---


## 🧩 Notas adicionales

- Asegúrate de que el servidor MySQL esté activo
- Verifica que los datos existen antes de hacer queries
- Habilita CORS si el frontend está en otro puerto

---

## 🧑‍💻 Autor

Desarrollado por **Brandon** como parte de una prueba técnica.

