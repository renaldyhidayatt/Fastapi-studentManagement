from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base


class FeedBackStudent(Base):
    __tablename__ = "feedback_student"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    feedback = Column(Text)
    reply = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    student = relationship("Student", backref="feedback_students")

    def __repr__(self) -> str:
        return "<FeedBackStudent(id='%s', student_id='%s', feedback='%s', reply='%s')>" % (
            self.id,
            self.student_id,
            self.feedback,
            self.reply,
        )
