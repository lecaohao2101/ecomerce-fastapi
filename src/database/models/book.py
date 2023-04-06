from sqlalchemy import String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base_class import Base


class BookModel(Base):
    name: Mapped[str] = mapped_column(
        String
    )
    description: Mapped[str] = mapped_column(
        String
    )
    price: Mapped[str] = mapped_column(
        Numeric
    )
    stock: Mapped[str] = mapped_column(
        Integer
    )
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("category.id")
    )
    store_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("store.id")
    )
    store: Mapped["StoreModel"] = relationship(
        "storeModel", lazy="subquery", back_populates="list_book"
    )
    category: Mapped["CategoryModel"] = relationship(
        "CategoryModel", lazy="subquery", back_populates="list_book"
    )
    list_book_order_item: Mapped["OrderItemModel"] = relationship(
         lazy="subquery", back_populates="list_book"
    )
    list_book_author: Mapped["AuthorModel"] = relationship(
         "AuthorModel", lazy="subquery", back_populates="book"
    )

    def __str__(self):
        return f'{self.name} {self.description}, {self.price}, {self.stock}, {self.store_id}, {self.category_id}'