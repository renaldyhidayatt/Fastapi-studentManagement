from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from src.config.database import get_db
from .courseschema import CourseSchema
from src.database.models.course import Course


router = APIRouter(prefix="/course", tags=["Course"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/")
async def create(request: CourseSchema, db: Session = Depends(get_db)):
    db_course = Course(name=request.name)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return Response("Berhasil membuat course", status_code=status.HTTP_201_CREATED)
