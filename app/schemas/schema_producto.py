from pydantic import BaseModel, Field, ConfigDict

class ProductoBase(BaseModel):
    nombre: str = Field(min_length=3, max_length=40)
    image_url: str 
    descripcion: str = Field(min_length=6)
    tamaño: str = Field(min_length=3)
    precio: float = Field(ge=1, le=100)

class ProductoRead(BaseModel):
    id: int
    nombre: str
    image_url: str
    descripcion: str
    precio: float
    tamaño: str


    model_config = ConfigDict(from_attributes=True)