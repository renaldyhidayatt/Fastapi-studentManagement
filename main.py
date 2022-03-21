import uvicorn
from fastapi import FastAPI
from config.database import create_table
from routes.auth import authrouter

app = FastAPI()



@app.on_event("startup")
async def runtimestartup():
    create_table()


@app.get("/")
def hello():
    return "hello";

app.include_router(authrouter.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
