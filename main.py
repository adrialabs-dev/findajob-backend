from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  email: str
  password: str


@app.get("/")
async def root():
  # return {"message": "Primer Mensaje"}
  return HTMLResponse("<h1>FindaJob API</h1>")

@app.post("/login", tags=["auth"])
async def login(user: User):
  return HTMLResponse("<h2>Login</h2>")