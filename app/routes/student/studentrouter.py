from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session

from app.config.database import get_db
from app.database.models.student import Student
from app.database.models.course import Course
from app.database.models.users import User

from .studentschema import StudentSchema

router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    return db.query(Student).join(Course, Student.course_id == Course.id, isouter=True).join(User, Student.user_id == User.id, isouter=True).all()


@router.post("/")
async def create(request: StudentSchema, db: Session = Depends(get_db)):

    db_student = Student(
        course_id=request.course_id,
        user_id=request.admin_id,
    )

    db.add(db_student)

    db.commit()

    return Response(
        content="Berhasil membuat user", status_code=status.HTTP_201_CREATED
    )



@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).join(Course, Student.course_id == Course.id, isouter=True).join(User, Student.user_id == User.id, isouter=True).filter(Student.id == id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.put("/{id}")
async def update(id: int,  db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return Response(content="Berhasil menghapus student", status_code=status.HTTP_200_OK)