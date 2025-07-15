from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from fastapi import Request, HTTPException, status
from app.models.model_cartitem import CartItem
from app.schemas.schema_cartitem import CreateCartItem
from app.jwt.core_security import get_user_from_request
from app.db.auxiliar import encontrar_user_email

def obtener_producto_carrito(request: Request, session: Session):
    email = get_user_from_request(request)
    user_db_id = encontrar_user_email(email, session)
    carrito = session.exec(select(CartItem).options(selectinload(CartItem.producto)).where(CartItem.user_id == user_db_id.id)).all()
    return carrito

def agregar_producto_carrito(data: CreateCartItem, request: Request, session: Session):
    email = get_user_from_request(request)
    user_id = encontrar_user_email(email, session)

    existing_producto = session.exec(select(CartItem).where(CartItem.user_id == user_id.id, CartItem.producto_id == data.producto_id)).first()
    if existing_producto:
        existing_producto.cantidad += data.cantidad
    else:
        producto_carrito = CartItem(user_id=user_id.id, producto_id=data.producto_id, cantidad=data.cantidad)
        session.add(producto_carrito)
    session.commit()
    
    productos_carrito_db_objects = session.exec(select(CartItem).options(selectinload(CartItem.producto)).where(CartItem.user_id == user_id.id)).all()

    return productos_carrito_db_objects

def eliminar_producto_carrito(cart_item_id: int, request: Request, session: Session):
    email = get_user_from_request(request)
    user_db_object = encontrar_user_email(email, session)

    if not user_db_object:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado.')
    
    cart_item_deleted = session.exec(select(CartItem).where(CartItem.user_id == user_db_object.id, CartItem.id == cart_item_id)).first()

    if not cart_item_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Producto del carrito no encontrado o no pertenece al usuario')

    session.delete(cart_item_deleted)
    session.commit()

    productos_carrito_actualizados = session.exec(select(CartItem).options(selectinload(CartItem.producto)).where(CartItem.user_id == user_db_object.id)).all()

    return productos_carrito_actualizados