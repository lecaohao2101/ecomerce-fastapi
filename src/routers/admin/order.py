from sqladmin import ModelView

from src.database.models import OrderModel
from src.helpers.permission import check_role_access, check_role_view


class OrderAdmin(ModelView, model=OrderModel):
    column_list = [OrderModel.id, OrderModel.created_date, OrderModel.total, OrderModel.order]
