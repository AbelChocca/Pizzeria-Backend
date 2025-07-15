from pydantic import BaseModel, ConfigDict, Field
from app.schemas.schema_producto import ProductoRead

class CreateCartItem(BaseModel):
    producto_id: int
    cantidad: int

class ReadCartItem(BaseModel):
    id: int 
    cantidad: int

    producto: ProductoRead

    model_config = ConfigDict(from_attributes=True)