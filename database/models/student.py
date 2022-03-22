from typing import Optional
from sqlalchemy.sql.expression import table
from sqlmodel import SQLModel
from sqlmodel.main import Field


class Student(SQLModel, table=True):
    """
    Student model

    """

    # admin_id =
    # admin =
    course: Optional[int] = Field(foreign_key="course.id", default=None)
