from jose import jwt, JWTError
from datetime import timedelta, timezone, datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generar_token(data: dict, expires: timedelta | None = None): 
    to_encode = data.copy()
    time_expiration = datetime.now(timezone.utc) + (expires or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp': time_expiration})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
    return payload