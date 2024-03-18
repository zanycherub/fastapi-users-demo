from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Temporary storage for registered users
users_db = []

class User(BaseModel):
    username: str
    email: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), email: str = Form(...)):
    user = User(username=username, email=email)
    users_db.append(user)
    return templates.TemplateResponse("register.html", {"request": request, "user": user})

@app.get("/users", response_class=HTMLResponse)
async def list_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})
