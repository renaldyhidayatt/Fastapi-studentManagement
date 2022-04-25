from fastapi import APIRouter, Depends, HTTPException, Response, status


from sqlalchemy.orm import Session
from config.database import get_db
from database.models.feedbackstaff import FeedBackStaff
from .fbstaffschema import FbStaffSchema


router = APIRouter(prefix="/fbstaff", tags=["FeedbackStaff"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/")
async def create(request: FbStaffSchema, db: Session = Depends(get_db)):
    db_fbstudent = FeedBackStaff(
        staff_id=request.staff_id,
        feedback=request.feedback,
        reply=request.reply,
    )

    db.add(db_fbstudent)

    db.commit()

    return Response(content="Berhasil Feedback", status_code=status.HTTP_201_CREATED)
