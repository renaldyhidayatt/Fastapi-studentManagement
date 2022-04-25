from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from src.config.database import get_db
from .adminschema import AdminSchema
from src.database.models.admin import Admin

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/hello")
async def hello():
    return {"msg": "Hello World"}


@router.post("/")
async def create(request: AdminSchema, db: Session = Depends(get_db)):
    db_admin = Admin(user_id=request.user_id)

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return Response("Berhasil membuat admin", status_code=status.HTTP_201_CREATED)
