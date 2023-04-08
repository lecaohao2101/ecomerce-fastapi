from sqladmin import ModelView
from src.database.models import AuthorModel


class AuthorAdmin(ModelView, model=AuthorModel):
    column_list = [AuthorModel.id, AuthorModel.name]
