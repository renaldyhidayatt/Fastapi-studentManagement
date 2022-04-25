from fastapi import APIRouter, Depends
from src.database.models.users import Users
from .userschema import UsersSchema

router = APIRouter(prefix="/users", tags=["Users"])
