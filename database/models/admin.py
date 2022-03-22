from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel
from sqlmodel.main import Field, Relationship
from .users import User

if TYPE_CHECKING:
    from .staff import Staff


class Admin(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    users_id: Optional[int] = Field(default=True, foreign_key="user.id")
    users: Optional[User] = Relationship(back_populates="admin")
    admin: Optional["Staff"] = Relationship(back_populates="admin")
