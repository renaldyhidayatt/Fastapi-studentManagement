from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="students")
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", backref="students")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return "<Student(id='%s', user_id='%s')>" % (self.id, self.user_id)