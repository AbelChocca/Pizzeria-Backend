from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    producto_id: int = Field(foreign_key="producto.id")
    cantidad: int = Field(default=1)

    producto: Optional["Producto"] = Relationship(back_populates='cart_items')


