from sqlmodel import SQLModel, Field
from typing import Annotated

class User(SQLModel, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    nombre: Annotated[str, Field(min_length=3, max_length=20)]
    email: str
    role: str = Field(default='user')
    hashed_password: str
    