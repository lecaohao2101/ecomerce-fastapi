from fastapi import FastAPI
from typing import List
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin
from sqlalchemy.orm import Session
from src.config import settings
from src.database.session import engine
from src.routers.admin.authentication import AdminAuth

from src.routers.admin.category import CategoryAdmin
from src.routers.admin.author import AuthorAdmin
from src.routers.admin.role import RoleAdmin
from src.routers.admin.user import UserAdmin
from src.routers.admin.address import AdressAdmin
from src.routers.admin.order import OrderAdmin
from src.routers.admin.store import StoreAdmin
from src.routers.admin.book import BookAdmin
from src.routers.admin.order_item import OrderItemAdmin
from src.routers.admin.customer import CustomerAdmin

from src.routers.ui_routes import router as ui_router
from src.routers.products import router as product_router
from src.database.models.user import UserModel
from src.database.models import user
# from fastapi_session import SessionMiddleware
from faker import Faker
fake = Faker()

if settings.debug == 'True':
    app = FastAPI(debug=True, reload=True)
else:
    app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(ui_router)
app.include_router(product_router)


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
# admin.add_view(CustomerAdmin)





