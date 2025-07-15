from passlib.context import CryptContext
from fastapi import Request, HTTPException, status
from app.jwt.jwt import verificar_token

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hashear_password(password: str) -> str:
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verificar_password(password: str, hashed_pass: str) -> bool:
    return pwd_context.verify(password, hashed_pass)

def get_token_from_cookie(request: Request):
    token = request.cookies.get('access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token no encontrado en el cookie')
    return token
def get_user_from_request(request: Request):
    token = get_token_from_cookie(request)
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')
    return payload.get('sub')