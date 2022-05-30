from fastapi import APIRouter, Depends, Response, status, HTTPException
from app.database.models.users import Users
from sqlalchemy.orm import Session
from app.config.database import get_db
from .userschema import UsersSchema

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/hello")
async def hello():
    return "Hello"


@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    return db.query(Users).all()


@router.post("/")
async def create(request: UsersSchema, db: Session = Depends(get_db)):
    db_users = Users(
        name=request.name,
        password=request.password,
        email=request.email
    )

    db.add(db_users)
    db.commit()
    db.refresh(db_users)

    return Response("Berhasil membuat users", status_code=status.HTTP_201_CREATED)

@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    users = db.query(Users).filter(Users.id == id).first()

    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    return users


@router.put("/{id}")
async def update(id: int, request: UsersSchema, db: Session = Depends(get_db)):
    users = db.query(Users).filter(Users.id == id).first()

    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    users.name = request.name
    users.password = request.password
    users.email = request.email

    db.add(users)
    db.commit()
    db.refresh(users)

    return Response("Berhasil mengubah users", status_code=status.HTTP_200_OK)


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    users = db.query(Users).filter(Users.id == id).first()

    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    db.delete(users)
    db.commit()

    return Response("Berhasil menghapus users", status_code=status.HTTP_200_OK)
    