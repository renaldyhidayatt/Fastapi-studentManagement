from sqlalchemy import Integer, String, DateTime, ForeignKey, Column
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    course_id = Column(Integer, ForeignKey("course.id"))
    date = Column(DateTime, default=func.now())
    status = Column(String, default="hadir")

    student = relationship("Student", backref="attendance")
    course = relationship("Course", backref="attendance")

    def __repr__(self) -> str:
        return "<Attendance(id='%s', student_id='%s', course_id='%s', date='%s', status='%s')>" % (
            self.id,
            self.student_id,
            self.course_id,
            self.date,
            self.status,
        )
