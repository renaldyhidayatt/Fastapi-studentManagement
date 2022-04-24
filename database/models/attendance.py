from sqlalchemy import Integer, String, DateTime, ForeignKey, Column
from sqlalchemy.sql import func
from config.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    course_id = Column(Integer, ForeignKey("course.id"))
    date = Column(DateTime, default=func.now())
    status = Column(String)
