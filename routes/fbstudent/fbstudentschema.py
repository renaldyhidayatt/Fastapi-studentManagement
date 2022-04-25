from pydantic import BaseModel


class FbStudentSchema(BaseModel):
    student_id: int
    feedback: str
    reply: str
