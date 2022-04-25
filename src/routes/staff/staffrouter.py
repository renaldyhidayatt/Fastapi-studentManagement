from fastapi import APIRouter, Depends, HTTPException, Response, status


from sqlalchemy.orm import Session
from src.config.database import get_db
from src.database.models.staff import Staff
from .staffschema import StaffSchema

router = APIRouter(prefix="/staff", tags=["Staff"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/")
async def create(request: StaffSchema, db: Session = Depends(get_db)):
    db_staff = Staff(
        user_id=request.user_id,
        course=request.course_id,
    )

    db.add(db_staff)

    db.commit()

    return Response(
        content="Berhasil membuat user", status_code=status.HTTP_201_CREATED
    )
