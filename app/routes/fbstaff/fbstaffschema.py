from pydantic import BaseModel


class FbStaffSchema(BaseModel):
    staff_id: int
    feedback: str
    reply: str
