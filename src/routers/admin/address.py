from sqladmin import ModelView

from src.database.models import AddressModel
from src.helpers.permission import check_role_access, check_role_view


class AdressAdmin(ModelView, model=AddressModel):
    column_list = [AddressModel.id, AddressModel.country, AddressModel.city, AddressModel.district, AddressModel.ward, AddressModel.street, AddressModel.number_home]
