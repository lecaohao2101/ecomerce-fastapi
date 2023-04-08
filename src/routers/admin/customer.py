from sqladmin import ModelView
from src.database.models import UserModel as CustomerModel


class CustomerAdmin(ModelView, model=CustomerModel):
    column_list = [CustomerModel.id, CustomerModel.email, CustomerModel.full_name, CustomerModel.role]
