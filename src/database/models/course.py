from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.config.database import Base


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
