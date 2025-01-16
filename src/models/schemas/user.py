from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class TokenPayload(BaseModel):
    sub: int
