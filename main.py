import uvicorn
from fastapi import FastAPI
from routes.auth import authrouter
from routes.admin import adminrouter
from routes.student import studentrouter
from routes.course import courserouter

from config.database import Base, engine

app = FastAPI()


@app.on_event("startup")
async def runtimestartup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return "hello"


app.include_router(authrouter.router)
app.include_router(adminrouter.router)
app.include_router(studentrouter.router)
app.include_router(courserouter.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
