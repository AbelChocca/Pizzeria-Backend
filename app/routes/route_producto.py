from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.schema_producto import ProductoBase, ProductoRead
from app.crud.crud_producto import obtener_productos, registrar_producto, obtener_productos_destacados, obtener_producto_por_id
from app.db.db import get_session

from typing import List, Optional

router = APIRouter(prefix='/productos', tags=['productos'])

@router.get('/destacados', response_model=List[ProductoRead])
def ObtenerProductosDestacados(session: Session = Depends(get_session)):
    return obtener_productos_destacados(session)

@router.get('/', response_model=List[ProductoRead])
def ObtenerProductos(session: Session = Depends(get_session), q: Optional[str] = None):
    return obtener_productos(session, q)

@router.get('/{nombre}', response_model=ProductoRead)
def ObtenerProductoPorNombre(nombre: str, session: Session = Depends(get_session)):
    return obtener_producto_por_id(nombre, session)

@router.post('/', response_model=ProductoRead)
def PublicarProducto(producto: ProductoBase, session: Session = Depends(get_session)):
    return registrar_producto(producto, session)