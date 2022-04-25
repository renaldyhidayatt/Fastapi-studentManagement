from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from src.config.database import get_db
from src.database.models.attendance import Attendance
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
