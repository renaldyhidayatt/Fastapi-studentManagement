from fastapi import APIRouter, Depends, HTTPException, Response, status
from src.utils.hashing import Hashing
from src.utils.token import Token

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm
from src.config.database import get_db
from .authschema import RegisterUser
from src.database.models.users import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/hello")
async def hello():
    return "Hello"


@router.post("/register")
async def register(request: RegisterUser, db: Session = Depends(get_db)):

    db_user = User(
        name=request.name,
        email=request.email,
        password=Hashing.create_hash(request.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return Response(
        content="Berhasil membuat user", status_code=status.HTTP_201_CREATED
    )


@router.post("/login")
async def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    if not Hashing.verify_hash(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = Token.create_access_token(data={"sub": user.email})
    response = {
        "name": user.name,
        "email": user.email,
        "jwtToken": access_token,
    }

    return response


@router.get("/getuser")
async def getUser(
    token: str = Depends(Token.get_currentUser), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == token).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    response = {"name": user.name, "email": user.email}

    return response
