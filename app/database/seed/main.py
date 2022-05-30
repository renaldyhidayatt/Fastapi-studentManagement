from ..models.admin import Admin
from sqlalchemy.orm import Session
from app.config.database import engine


def admincreate():
    db = Session(engine)
    db_admin = Admin(user_id=1)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
