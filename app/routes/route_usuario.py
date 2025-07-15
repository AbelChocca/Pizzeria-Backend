from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import HTTPBearer
from sqlmodel import Session
from app.db.db import get_session
from app.schemas.schema_usuario import ReadUser, CreateUser, LoginRequest
from app.crud.crud_usuario import crear_usuario,obtener_usuarios, loggear_usuario, obtener_usuario, cerrar_session
from app.jwt.core_security import get_token_from_cookie
from typing import List

router = APIRouter(prefix='/usuarios', tags=['users'])

oauth2_schema = HTTPBearer()

@router.get('/', response_model=List[ReadUser])
def LeerUsuarios(session: Session = Depends(get_session)):
    return obtener_usuarios(session)

@router.post('/', response_model=ReadUser)
def RegistrarUsuario(user: CreateUser, session: Session = Depends(get_session)):
    return crear_usuario(user, session)

@router.post('/login')
def UserLogin(data: LoginRequest, response: Response, session: Session = Depends(get_session)):
    token = loggear_usuario(data, session)
    if not token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Credenciales incorretos')
    

    response.set_cookie(
        key='access_token',
        value=token,
        max_age=3600,
        path='/',
        httponly=True,
        samesite='none',
        secure=True
    )
    return {"mensaje": "Login exitoso"}
    
@router.post('/logout', status_code=status.HTTP_204_NO_CONTENT)
def Logout(response: Response):
    return cerrar_session(response)

@router.get('/me', response_model=ReadUser)
def ObtenerUsuario(request: Request, session: Session = Depends(get_session)):
    token = get_token_from_cookie(request)
    user = obtener_usuario(token, session)
    return user
    
