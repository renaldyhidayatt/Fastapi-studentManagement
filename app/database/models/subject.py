from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    course_id = Column(Integer, ForeignKey("course.id"))
    staff = relationship("Staff", backref="subjects")
    course = relationship("Course", backref="subjects")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return "<Subject(id='%s', name='%s', staff_id='%s', course_id='%s')>" % (
            self.id,
            self.name,
            self.staff_id,
            self.course_id,
        )
