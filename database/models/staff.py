from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.database import Base


class StaffModel(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey("admin.id"))
    admin = relationship("User", uselist=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
