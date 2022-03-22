from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel.main import Relationship

from models.admin import Admin


class Staff(SQLModel, table=True):
    id: Optional[int] = Field(index=True, primary_key=True)
    course_id: Optional[int] = Field(default=True, foreign_key="course.id")
    admin_id: Optional[int] = Field(default=True, foreign_key="admin.id")
    admin: Optional[Admin] = Relationship(back_populates="admin")
