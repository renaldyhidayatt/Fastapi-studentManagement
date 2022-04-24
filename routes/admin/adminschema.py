from pydantic import BaseModel


class AdminSchema(BaseModel):
    user_id: int
