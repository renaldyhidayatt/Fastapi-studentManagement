from typing import Optional
from pydantic import BaseModel
from routes.users.userschema import UsersSchema
from routes.course.courseschema import CourseSchema


class StudentSchema(BaseModel):
    admin_id: int
    course_id: int


class StudentSchemaResponse(StudentSchema):

    user: Optional[UsersSchema] = None
    course: Optional[CourseSchema] = None

    class Config:
        orm_mode = True
