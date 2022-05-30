from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.database.models.student import Student
from app.database.models.course import Course

from sqlalchemy.orm import Session
from app.config.database import get_db
from app.database.models.attendance import Attendance
from .attendanceschema import AttendanceSchema

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/")
async def create(request: AttendanceSchema, db: Session = Depends(get_db)):
    db_attendance = Attendance(
        student_id=request.student_id,
        subject_id=request.subject_id,
        status=request.status,
    )

    db.add(db_attendance)

    db.commit()

    return Response(content="Berhasil Attendance", status_code=status.HTTP_201_CREATED)


@router.get("/")
def getAll(db: Session = Depends(get_db)):
    attendance = db.query(Attendance).join(Student, Attendance.student_id == Student.id, isouter=True).join(Course, Attendance.course_id == Course.id, isouter=True).all()

    return Response(content=attendance, status_code=status.HTTP_200_OK)


@router.get("/{id}")
def getById(id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).join(Student, Attendance.student_id == Student.id, isouter=True).join(Course, Attendance.course_id == Course.id, isouter=True).filter(Attendance.id == id).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    return Response(content=attendance, status_code=status.HTTP_200_OK)


@router.put("/{id}")
def update(id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.id == id).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    return Response(content="Berhasil mengubah attendance", status_code=status.HTTP_200_OK)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.id == id).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    db.delete(attendance)
    db.commit()

    return Response(content="Berhasil menghapus attendance", status_code=status.HTTP_200_OK)