from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from src.config import settings
from src.database.session import engine
from src.routers.admin.authentication import AdminAuth
from src.routers.admin.role import RoleAdmin
from src.routers.admin.user import UserAdmin
from src.routers.ui_routes import router as ui_router
from src.routers.products import router as product_router

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
admin.add_view(UserAdmin)
admin.add_view(RoleAdmin)
