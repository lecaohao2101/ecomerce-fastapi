from sqladmin import ModelView

from src.database.models import AuthorModel
from src.helpers.permission import check_role_access, check_role_view


class AuthorAdmin(ModelView, model=AuthorModel):
    column_list = [AuthorModel.id, AuthorModel.name]
