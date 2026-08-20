from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# كنقراو ملف .env اللي درناه فالاول
load_dotenv()

app = FastAPI(title="Nidde Demo API")

# النموذج ديال البيانات اللي غادي يدخلها الادمن
class AdminLogin(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Nidde API is running"}

@app.post("/admin/login")
def admin_login(data: AdminLogin):
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if data.email == admin_email and data.password == admin_password:
        return {"success": True, "message": "Login successful. Welcome Admin"}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
