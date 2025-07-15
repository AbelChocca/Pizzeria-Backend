from sqlmodel import SQLModel, Field, Relationship
from typing import Annotated, List

class Producto(SQLModel, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    nombre: str
    image_url: str
    descripcion: str
    precio: float
    tamaño: str

    cart_items: List["CartItem"] = Relationship(back_populates='producto')

