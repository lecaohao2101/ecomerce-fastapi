from sqladmin import ModelView

from src.database.models import OrderItemModel
from src.helpers.permission import check_role_access, check_role_view


class OrderItemAdmin(ModelView, model=OrderItemModel):
    column_list = [OrderItemModel.id, OrderItemModel.book, OrderItemModel.order, OrderItemModel.quantity, OrderItemModel.subtotal]
