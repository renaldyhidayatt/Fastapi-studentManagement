import uvicorn
from fastapi import FastAPI
from src.routes.auth import authrouter
from src.routes.admin import adminrouter
from src.routes.student import studentrouter
from src.routes.course import courserouter
from src.routes.subject import subjectrouter
from src.routes.staff import staffrouter
from src.routes.attendance import attendancerouter
from src.routes.fbstudent import fbstudentrouter
from src.routes.fbstaff import fbstaffrouter
from src.database.seed.main import admincreate

from src.config.database import Base, engine

app = FastAPI()


@app.on_event("startup")
async def runtimestartup():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def runtimeseed():
    admincreate()


@app.get("/")
def hello():
    return "hello"


app.include_router(authrouter.router)
app.include_router(adminrouter.router)
app.include_router(studentrouter.router)
app.include_router(courserouter.router)
app.include_router(subjectrouter.router)
app.include_router(staffrouter.router)
app.include_router(attendancerouter.router)
app.include_router(fbstudentrouter.router)
app.include_router(fbstaffrouter.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
