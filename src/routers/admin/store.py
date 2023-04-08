from sqladmin import ModelView
from src.database.models import StoreModel


class StoreAdmin(ModelView, model=StoreModel):
    column_list = [StoreModel.id, StoreModel.name, StoreModel.user]
