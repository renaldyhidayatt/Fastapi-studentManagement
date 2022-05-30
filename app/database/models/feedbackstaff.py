from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.config.database import Base
from sqlalchemy.orm import relationship


class FeedBackStaff(Base):
    __tablename__ = "feedback_staff"

    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.id"))
    staff = relationship("Staff", backref="feedback_staffs")
    feedback = Column(Text)
    reply = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return "<FeedBackStaff(id='%s', staff_id='%s', feedback='%s', reply='%s')>" % (
            self.id,
            self.staff_id,
            self.feedback,
            self.reply,
        )