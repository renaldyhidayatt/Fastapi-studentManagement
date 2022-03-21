from sqlmodel import create_engine
from sqlmodel.main import SQLModel

SQLALCHAMY_DATABASE_URL = "postgresql://postgres:@localhost/studentmanagement"
engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True)


def create_table():
    SQLModel.metadata.create_all(engine)