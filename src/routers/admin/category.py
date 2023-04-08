from sqladmin import ModelView
from src.database.models import CategoryModel


class CategoryAdmin(ModelView, model=CategoryModel):
    column_list = [CategoryModel.id, CategoryModel.name]
