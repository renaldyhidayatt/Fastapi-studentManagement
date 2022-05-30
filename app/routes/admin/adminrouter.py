from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.orm import Session
from app.config.database import get_db
from .adminschema import AdminSchema
from app.database.models.admin import Admin
from app.database.models.users import User

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/hello")
async def hello():
    return {"msg": "Hello World"}


@router.get("/")
def getAll(db: Session = Depends(get_db)):
    admin = db.query(Admin).join(User, Admin.user_id == User.id, isouter=True).all()
 
    return admin

@router.post("/")
async def create(request: AdminSchema, db: Session = Depends(get_db)):
    db_admin = Admin(user_id=request.user_id)

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return Response("Berhasil membuat admin", status_code=status.HTTP_201_CREATED)


@router.get("/{id}")
def getById(id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == id).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return admin


@router.put("/{id}")
def update(id: int,  db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == id).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    
    return admin


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == id).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    db.delete(admin)
    db.commit()

    return Response("Berhasil menghapus admin", status_code=status.HTTP_200_OK)
