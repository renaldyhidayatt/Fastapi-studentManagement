from pydantic import BaseModel


class StaffSchema(BaseModel):
    user_id: int
    course_id: int
