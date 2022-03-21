from fastapi import APIRouter,Depends,HTTPException, Response, status
from utils.hashing import Hashing
from utils.token import Token


from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from config.database import engine
from .authschema import RegisterUser
from  database.models.users import Users

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/hello")
async def hello():
    return "Hello"

@router.post("/register")
async def register(request: RegisterUser):
    db = Session(engine)
    db_user = Users(
        name=request.name,
        email=request.email,
        password=Hashing.create_hash(request.password)
    )

    db.add(db_user)
    db.commit()


    return Response(content="Berhasil membuat user", status_code=status.HTTP_201_CREATED)

    

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    db = Session(engine)

    user = db.query(Users).filter(Users.email == request.username).first()

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
async def getUser(token: str = Depends(Token.get_currentUser)):
    db = Session(engine)
    user = db.query(Users).filter(Users.email == token).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )

    response = {
        "name": user.name,
        "email": user.email
    }

    return response