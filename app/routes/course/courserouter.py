from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from app.config.database import get_db
from .courseschema import CourseSchema
from app.database.models.course import Course


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


@router.get("/")
def getAll(db: Session = Depends(get_db)):
    course = db.query(Course).all()

    return course


@router.get("/{id}")
def getById(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course


@router.put("/{id}")
def update(id: int, request: CourseSchema, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    course.name = request.name

    db.add(course)
    db.commit()
    db.refresh(course)

    return Response("Berhasil mengubah course", status_code=status.HTTP_200_OK)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(course)
    db.commit()

    return Response("Berhasil menghapus course", status_code=status.HTTP_200_OK)