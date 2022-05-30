import uvicorn
from fastapi import FastAPI

from app.routes.auth import authrouter



from app.routes.admin import adminrouter
from app.routes.student import studentrouter
from app.routes.course import courserouter
from app.routes.subject import subjectrouter
from app.routes.staff import staffrouter
from app.routes.attendance import attendancerouter
from app.routes.fbstudent import fbstudentrouter
from app.routes.fbstaff import fbstaffrouter
from app.database.seed.main import admincreate

from app.config.database import Base, engine

app = FastAPI(
    title="API for Student Management",
    description="This is a API for Student Management",
    version="1.0.0",
)


@app.on_event("startup")
async def runtimestartup():
    Base.metadata.create_all(bind=engine)


# @app.on_event("startup")
# async def runtimeseed():
#     admincreate()


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
