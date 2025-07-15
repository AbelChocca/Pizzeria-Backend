from sqlmodel import Session, select
from app.models.model_usuario import User


def encontrar_user_email(email: str, session: Session):
    user = session.exec(select(User).where(User.email == email)).first()
    return user