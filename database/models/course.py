from typing import Optional
from sqlmodel import SQLModel, Field


class Course(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)
