from pydantic import BaseModel


class AttendanceSchema(BaseModel):
    student_id: int
    course_id: int
    status: str
