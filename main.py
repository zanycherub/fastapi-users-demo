from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
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

def authenticate_user(email: str, password: str):
    for user in users_db:
        if user.email == email:
            return True
    return False

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...),):
    if authenticate_user(email, password):
        return {"message": "authentication successful"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), email: str = Form(...)):
    user = User(username=username, email=email)
    users_db.append(user)
    return templates.TemplateResponse("success.html", {"request": request, "user": user})

@app.get("/users", response_class=HTMLResponse)
async def list_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})


