from sqlmodel import Session, select
from app.models.model_producto import Producto
from app.schemas.schema_producto import ProductoBase
from typing import Optional

def obtener_productos_destacados(session: Session):
    return session.exec(select(Producto).where(Producto.id <= 10)).all()

def obtener_productos(session: Session, q: Optional[str] = None):
    query = select(Producto)
    if q:
        pattern = f'%{q.lower()}%'

        query = query.where(
            Producto.nombre.ilike(pattern) |
            Producto.descripcion.ilike(pattern)
        )
        
    return session.exec(query).all()

def obtener_producto_por_id(nombre: str, session: Session):
    producto = select(Producto).where(Producto.nombre == nombre)
    return session.exec(producto).first()

def registrar_producto(producto: ProductoBase, session: Session):
    model_producto = Producto(**producto.model_dump())
    session.add(model_producto)
    session.commit()
    session.refresh(model_producto)
    return model_producto