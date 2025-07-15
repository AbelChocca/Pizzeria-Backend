from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CreateUser(BaseModel):
    nombre: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(min_length=6)

class LoginRequest(BaseModel):
    username: str 
    password: str

class ReadUser(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

class UpdateUser(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=30) 
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)
