from fastapi import status, HTTPException, Response
from sqlmodel import Session, select
from app.db.auxiliar import encontrar_user_email
from app.jwt.jwt import verificar_token
from app.jwt.core_security import hashear_password, verificar_password
from app.jwt.jwt import generar_token
from app.schemas.schema_usuario import CreateUser, LoginRequest
from app.models.model_usuario import User


def obtener_usuarios(session: Session):
    return session.exec(select(User)).all()

def crear_usuario(user: CreateUser, session: Session):
    user_db = encontrar_user_email(user.email, session)
    if user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario ya registrado')
    hashed_password = hashear_password(user.password)
    user_registrado = User(nombre=user.nombre, email=user.email, role='user', hashed_password=hashed_password)
    session.add(user_registrado)
    session.commit()
    session.refresh(user_registrado)
    return user_registrado

def loggear_usuario(data: LoginRequest, session: Session):
    user = encontrar_user_email(data.username, session)
    if not user or not verificar_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Correo o contraseña invalidos')
    token = generar_token({'sub': user.email})
    return token

def cerrar_session(response: Response):
    response.delete_cookie(
        key='access_token',
        path='/'
    )
    return 

def obtener_usuario(token: str, session: Session):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Token invalido')
    email = payload.get('sub')
    user = encontrar_user_email(email, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    return user
    