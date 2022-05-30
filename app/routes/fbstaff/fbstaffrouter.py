from fastapi import APIRouter, Depends, HTTPException, Response, status


from sqlalchemy.orm import Session
from app.config.database import get_db
from app.database.models.feedbackstaff import FeedBackStaff
from app.database.models.staff import Staff
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

@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    staff = db.query(FeedBackStaff).join(Staff, FeedBackStaff.staff_id == Staff.id, isouter=True).all()

    return staff


@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    staff = db.query(FeedBackStaff).join(Staff, FeedBackStaff.staff_id == Staff.id, isouter=True).filter(FeedBackStaff.id == id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Feedback not found")

    return staff


@router.put("/{id}")
async def update(id: int, db: Session = Depends(get_db)):
    staff = db.query(FeedBackStaff).filter(FeedBackStaff.id == id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Feedback not found")

    return Response(content="Berhasil mengubah feedback", status_code=status.HTTP_200_OK)


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    staff = db.query(FeedBackStaff).filter(FeedBackStaff.id == id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Feedback not found")

    db.delete(staff)
    db.commit()

    return Response(content="Berhasil menghapus feedback", status_code=status.HTTP_200_OK)