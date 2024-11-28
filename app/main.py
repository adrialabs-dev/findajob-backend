from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from db import  create_all_tables
from .routers import job


app = FastAPI(lifespan=create_all_tables)
app.include_router(job.job_router)


class User(BaseModel):
    email: str
    password: str


@app.get("/")
async def root():
    return HTMLResponse("<h1>FindaJob API</h1>")


@app.post("/login", tags=["Auth"])
async def login(user: User):
    return HTMLResponse("<h2>Login</h2>")


