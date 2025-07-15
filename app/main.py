from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.db import init_db
from fastapi.middleware.cors import CORSMiddleware
from app.routes import route_usuario, route_producto, route_cartitem
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Iniciando App')
    init_db()
    yield
    print('Finalizando App')

app = FastAPI(title='Pizzeria Angelita', lifespan=lifespan)

origins = ["http://localhost:5173", "https://pizzeria-frontend.up.railway.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(route_usuario.router)
app.include_router(route_producto.router)
app.include_router(route_cartitem.router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
