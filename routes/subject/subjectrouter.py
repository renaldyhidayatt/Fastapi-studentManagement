from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from config.database import get_db
from database.models.subject import Subject
from .subjectschema import SubjectSchema


router = APIRouter(prefix="/subject", tags=["Subject"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/")
async def create(request: SubjectSchema, db: Session = Depends(get_db)):
    db_subject = Subject(
        name=request.name,
        staff=request.staff_id,
        course=request.course_id,
    )

    db.add(db_subject)

    db.commit()

    return Response(
        content="Berhasil membuat user", status_code=status.HTTP_201_CREATED
    )
