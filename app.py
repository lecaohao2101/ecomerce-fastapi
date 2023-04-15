from fastapi import FastAPI, Depends, HTTPException, Request, Form, status
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from src.database.models import RoleModel
from src.routers.admin.address import AdressAdmin
from src.routers.admin.authentication import AdminAuth
from src.routers.admin.author import AuthorAdmin
from src.routers.admin.book import BookAdmin
from src.routers.admin.category import CategoryAdmin
from src.routers.admin.order import OrderAdmin
from src.routers.admin.order_item import OrderItemAdmin
from src.routers.admin.role import RoleAdmin
from src.routers.admin.user import UserAdmin
from src.routers.admin.store import StoreAdmin
from src.routers.register.register import templates
# from src.routers.admin.request import Request
from src.routers.ui_routes import router as ui_router
from src.routers.products import router as product_router
from src.database.models.user import UserModel
from src.database.session import *


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# if settings.debug == 'True':
#     app = FastAPI(debug=True, reload=True)
# else:
#     app = FastAPI()

app.mount("/static", StaticFiles(directory  ="src/static"), name="static")

app.include_router(ui_router)
app.include_router(product_router)

#ADMIN
authentication_backend = AdminAuth(secret_key="app-dev")
admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=authentication_backend
)


admin.add_view(RoleAdmin)
admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(AdressAdmin)
admin.add_view(OrderAdmin)
admin.add_view(StoreAdmin)
admin.add_view(BookAdmin)
admin.add_view(OrderItemAdmin)
# admin.add_view(Request)



# @app.post("/register")
# async def register_user(email: str, full_name: str, password: str, ward: str, street: str, number_home: int):
#     # Save the user data to the database using SQLAlchemy
#     # ...
#     return {"message": "User registered successfully"}

@app.post("/register")
async def register(
        request: Request,
    role_id:int=Form(default=3),
    email: str = Form(default=None),
    full_name: str = Form(default=None),
    password: str = Form(default=None),
    re_password: str = Form(default=None),
    session: Session = Depends(get_db)
):
    # if password != re_password:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password does not match")
    #
    # user = UserModel(role_id=role_id, email=email, full_name=full_name, password=password)
    # session.add(user)
    # session.commit()


    # return {"message": "User created successfully"}
    if password != re_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password does not match")

    user = UserModel(role_id=role_id, email=email, full_name=full_name, password=password)
    session.add(user)
    session.commit()

    return templates.TemplateResponse("page-sign-in.html", {"request": request})
# @app.post('add_new_user')
# def add_new_user(email: UserModel, db:Session=Depends(get_db)):
#     email = get_user_by_email(db=db, email=email.email)
#     if email:
#         raise HTTPException(status_code=400, detail=f"Email{email.email} already exist in databse: {email}")
#     return add_new_user(db=db, email=email)



# Định nghĩa schema cho API
# class UserCreate(BaseModel):
#     role_id:int
#     full_name: str
#     email: str
#     password: str

# Đăng ký người dùng mới
# @app.post("/register")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = UserModel(full_name=user.full_name, email=user.email, password=user.password, role_id = user.role_id)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# templates = Jinja2Templates(directory="templates")
#
# Base.metadata.create_all(bind=engine)
#
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# @app.post("/register", response_class=HTMLResponse)
# async def register(
#     request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)
# ):
#     db_user = models.UserModel(email=user.email, full_name=user.full_name, password=user.password, role_id=user.role_id)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return templates.TemplateResponse("pages/index.html", {"request": request, "user": db_user})

# templates = Jinja2Templates(directory="templates")
#
# Base.metadata.create_all(bind=engine)
# @app.post("/register", response_class=HTMLResponse)
# async def register(request: Request, user: UserCreate, db: Session = Depends(get_db)):
#     db_user = UserModel(
#         email=user.email,
#         full_name=user.full_name,
#         password=user.password,
#         role_id=user.role_id
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return templates.TemplateResponse("pages/index.html", {"request": request, "user": db_user})