from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from app.db.db import get_session
from app.crud.crud_cartitem import obtener_producto_carrito, agregar_producto_carrito, eliminar_producto_carrito
from app.schemas.schema_cartitem import ReadCartItem, CreateCartItem
from typing import List


router = APIRouter(prefix='/carrito', tags=['carrito_de_compras'])

@router.get('/', response_model=List[ReadCartItem])
def ObtenerCarrito(request: Request, session: Session = Depends(get_session)):
    return obtener_producto_carrito(request, session)

@router.post('/', response_model=List[ReadCartItem])
def AgregarAlCarrito(data: CreateCartItem, request: Request, session: Session = Depends(get_session)):
    return agregar_producto_carrito(data, request, session)

@router.delete('/{cart_item_id}', response_model=List[ReadCartItem])
def EliminarItemCarrito(cart_item_id: int, request: Request, session: Session = Depends(get_session)):
    return eliminar_producto_carrito(cart_item_id, request, session)