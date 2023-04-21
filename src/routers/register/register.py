# from fastapi import FastAPI
# from sqlalchemy.orm import Session
# from src.schemas import UserAdd
# from src.database.models.user import UserModel
#
#
#
# # @app.post("/register")
# # async def register_user(username: str, password: str, email: str):
# #     # Code để xử lý thông tin đăng ký sẽ được thêm ở bước sau
# #     return {"message": "User registered successfully"}
# # def create_user(db: Session, user: UserCreate):
# #     db_user = UserModel(email=user.email, password=user.password, full_name=user.full_name)
# #     db.add(db_user)
# #     db.commit()
# #     db.refresh(db_user)
# #     return db_user
#
# def add_user(db: Session, user:UserAdd):
#     user_details = UserModel(
#         email = user.email,
#         full_name = user.full_name,
#         password = user.password
#     )
#     db.add(add_user)
#     db.commit()
#     db.refresh()
#     return UserModel(**user.dict())
#
# def get_user_by_email(db:Session, email:str):
#     return db.query(UserModel).filter(UserModel.email==email).first()

from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.database.session import SessionLocal
from src.database.models import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register_post(request: Request, db: Session = Depends(get_db),
                        email: str = Form(...), full_name: str = Form(...),
                        password: str = Form(...), role_id: int = Form(...)):
    user = UserCreate(email=email, full_name=full_name, password=password, role_id=role_id)
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return templates.TemplateResponse("register.html", {"request": request})
