from sqladmin import ModelView
from src.database.models import OrderModel


class OrderAdmin(ModelView, model=OrderModel):
    column_list = [OrderModel.id, OrderModel.created_date, OrderModel.total, OrderModel.order]
