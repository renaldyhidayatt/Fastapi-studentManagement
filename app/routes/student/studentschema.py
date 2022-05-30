from pydantic import BaseModel


class StudentSchema(BaseModel):
    admin_id: int
    course_id: int
