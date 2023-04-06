from sqlalchemy import String, Integer, ForeignKey, DateTime, Double
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base_class import Base


class StoreModel(Base):
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id")
    )
    name: Mapped[str] = mapped_column(
        String
    )
    user: Mapped["UserModel"] = relationship(
        "UserModel", lazy="subquery", back_populates="list_store"
    )
    list_book: Mapped["BookModel"] = relationship(
        "BookModel", lazy="subquery", back_populates="store"
    )
    def __str__(self):
        return f'{self.name}'