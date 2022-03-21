from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class Users(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    email: str
    password: str