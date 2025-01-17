from sqlmodel import Session, select
from typing import Optional

from src.models.models import User
from src.models.schemas import user
from src.core.security import get_password_hash, verify_password

def create_user(*,session: Session, user_create: user.UserCreate) -> User:
    db_user = User(
        name=user_create.name,
        email=user_create.email,
        hashed_password=get_password_hash(user_create.password),
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_user_by_email(*,session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    result = session.exec(statement).first()
    return result

def update_user(*,session: Session, db_user: User, user_update: user.UserUpdate) -> User:
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def delete_user(*,session: Session, user_id: int) -> Optional[User]:
    db_user = session.get(User, user_id)
    if db_user:
        session.delete(db_user)
        session.commit()
    return db_user
