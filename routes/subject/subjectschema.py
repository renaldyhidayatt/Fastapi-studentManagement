import imp
from pydantic import BaseModel


class SubjectSchema(BaseModel):
    name: str
    staff_id: int
    course_id: int
