from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.models.schemas import user
from src.services import user_service
from sqlmodel import select

from src.api.dependencies import SessionDep

router = APIRouter()

@router.post("/", response_model=user.User)
def create_user(*, session: SessionDep, user: user.UserCreate):
    db_user = user_service.get_user_by_email(session=session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(session=session, user_create=user)

@router.get("/{user_id}", response_model=user.User)
def read_user(*, session: SessionDep, user_id: int):
    db_user = session.get(user.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[user.User])
def read_users(*, session: SessionDep, skip: int = 0, limit: int = 10):
    statement = select(user.User).offset(skip).limit(limit)
    return session.exec(statement).all()

@router.put("/{user_id}", response_model=user.User)
def update_user(*, session: SessionDep, user_id: int, user: user.UserUpdate):
    db_user = session.get(user.User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_service.update_user(session=session, db_user=db_user, user_update=user)

@router.delete("/{user_id}", response_model=user.User)
def delete_user(*, session: SessionDep, user_id: int):
    db_user = user_service.delete_user(session=session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
