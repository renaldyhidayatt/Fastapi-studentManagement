from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship

from sqlalchemy import Column, String

if TYPE_CHECKING:
    from .admin import Admin


class User(SQLModel, table=True):
    id: Optional[int] = Field(index=True, primary_key=True)
    name: str
    email: str = Field(sa_column=Column("email", String, unique=True))
    password: str
    image: Optional[str] = Field(default=None)
    created_at: Optional[str] = Field(index=True)
    updated_at: Optional[str] = Field(index=True)
    admin: List["Admin"] = Relationship(back_populates="users")
