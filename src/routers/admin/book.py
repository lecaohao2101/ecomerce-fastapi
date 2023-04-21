from sqladmin import ModelView
from src.database.models import BookModel
from src.helpers.permission import check_role_access, check_role_view


class BookAdmin(ModelView, model=BookModel):
    name_plural = "Book"
    icon = "fa-solid fa-book"
    column_list = [BookModel.id, BookModel.name, BookModel.price, BookModel.stock,
    BookModel.category, BookModel.created_at,BookModel.updated_at]
    column_details_exclude_list = [BookModel.store_id,BookModel.id,BookModel.category_id,BookModel.author_id,BookModel.list_book_order_item]
    column_searchable_list=[BookModel.name]

    def is_accessible(self, request) -> bool:
        return check_role_access(request)

    def is_visible(self, request) -> bool:
        return check_role_view(request, self.identity)