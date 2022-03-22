from typing import Optional
from pydantic import BaseModel

class UsersSchema(BaseModel):
    name: str
    email: str
    created_at: Optional[str]
    updated_at: Optional[str]

