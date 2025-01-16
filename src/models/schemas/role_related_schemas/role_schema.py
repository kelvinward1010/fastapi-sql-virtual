from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class UserRoles(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"


class RoleBase(SQLModel):
    role_name: str = Field(max_length=50, nullable=False, unique=True)


class RoleCountResponse(SQLModel):
    role_name: str
    quantity: int


class RoleUpdate(BaseModel):
    user_id: UUID
    role_id: UUID


class RolePublic(RoleBase):
    id: UUID
