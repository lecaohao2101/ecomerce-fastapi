from sqladmin import ModelView
from src.database.models import OrderItemModel


class OrderItemAdmin(ModelView, model=OrderItemModel):
    column_list = [OrderItemModel.id, OrderItemModel.book, OrderItemModel.order, OrderItemModel.quantity, OrderItemModel.subtotal]
