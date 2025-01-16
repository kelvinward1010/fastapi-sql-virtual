from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str
