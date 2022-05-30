from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from app.config.database import get_db
from app.database.models.subject import Subject
from app.database.models.course import Course
from app.database.models.staff import Staff
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
        content="Berhasil membuat subject", status_code=status.HTTP_201_CREATED
    )


@router.get("/")
def getAll(db: Session = Depends(get_db)):
    subject = db.query(Subject).join(Course, Subject.course_id == Course.id, isouter=True).join(Staff, Subject.staff_id == Staff.id, isouter=True).all()

    return subject


@router.get("/{id}")
def getById(id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).join(Course, Subject.course_id == Course.id, isouter=True).join(Staff, Subject.staff_id == Staff.id, isouter=True).filter(Subject.id == id).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return subject


@router.put("/{id}")
def update(id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == id).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return Response(content="Berhasil mengubah subject", status_code=status.HTTP_200_OK)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == id).first()

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return Response(content="Berhasil menghapus subject", status_code=status.HTTP_200_OK)
    