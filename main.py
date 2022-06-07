from fastapi import FastAPI

from .routers import (
    user,
    student
)

app = FastAPI()

app.include_router(user.router,tags=["User"], prefix="/user")
app.include_router(student.router, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
