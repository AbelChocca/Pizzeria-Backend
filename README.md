<img src="https://st4.depositphotos.com/3316741/22997/i/450/depositphotos_229976142-stock-photo-pizza-with-tomatoes-mozzarella-cheese.jpg"
    alt="Pizzeria banner"
    width="600" />

# Pizzeria-Backend API
API REST construida con FastAPI, SQLModel y PostgreSQL para gestionar pedidos, usuarios y autenticación JWT de una pizzería, lista para producción con Docker y Railway.

# Características
✅ CRUD de usuarios con autenticación JWT.
✅ Gestión de pedidos y productos.
✅ Conexión a PostgreSQL usando SQLModel.
✅ Arquitectura limpia y modular.
✅ CORS configurado para frontend en Railway.
✅ Listo para CI/CD con GitHub Actions y despliegue en Railway.

# Tecnologías utilizadas
FastAPI 

SQLModel

PostgreSQL

Docker

Uvicorn

Railway para despliegue

GitHub Actions para CI/CD

# Instalacion local

## Clonar repositorio:
git clone https://github.com/AbelChocca/Pizzeria-Backend.git
cd Pizzeria-Backend

## Instalar dependencias:
pip install -r requirements.txt

## Configurar variables de entorno creando un archivo .env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
JWT_SECRET=tu_secret

## Ejecutar servidor:
uvicorn app.main:app --reload

## Abrir en el navegador:
http://localhost:8000/docs