from pydantic import BaseModel


class CourseSchema(BaseModel):
    name: str
