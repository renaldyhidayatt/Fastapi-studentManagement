from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session

from config.database import get_db
from database.models.student import Student

from .studentschema import StudentSchema, StudentSchemaResponse

router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    return db.query(Student).all()


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
