from sqladmin import ModelView

from src.database.models import CategoryModel
from src.helpers.permission import check_role_access, check_role_view


class CategoryAdmin(ModelView, model=CategoryModel):
    column_list = [CategoryModel.id,CategoryModel.name]
