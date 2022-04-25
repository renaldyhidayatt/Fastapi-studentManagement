from fastapi import APIRouter, Depends, HTTPException, Response, status


from sqlalchemy.orm import Session
from src.config.database import get_db
from src.database.models.feedbackestudent import FeedBackStudent
from .fbstudentschema import FbStudentSchema


router = APIRouter(prefix="/fbstudent", tags=["FeedbackStudent"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/")
async def create(request: FbStudentSchema, db: Session = Depends(get_db)):
    db_fbstudent = FeedBackStudent(
        student_id=request.student_id,
        feedback=request.feedback,
        reply=request.reply,
    )

    db.add(db_fbstudent)

    db.commit()

    return Response(content="Berhasil Feedback", status_code=status.HTTP_201_CREATED)
