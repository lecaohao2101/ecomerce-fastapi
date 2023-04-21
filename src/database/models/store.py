from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy.types import
from sqlalchemy.orm import declarative_base
from sqlalchemy_fields.storages import FileSystemStorage
from sqlalchemy_fields.types import ImageType
from src.database.base_class import Base
from sqlalchemy import LargeBinary


class StoreModel(Base, ):
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id")
    )
    name: Mapped[str] = mapped_column(
        String
    )
    image: Mapped[str] = mapped_column(
        String
    )
    # image: Mapped[bytes] = Column(LargeBinary)
    # image: Mapped[bytes] = mapped_column(
    #     ImageType
    # )
    user: Mapped["UserModel"] = relationship(
        "UserModel", lazy="subquery", back_populates="list_store"
    )
    list_book: Mapped["BookModel"] = relationship(
        "BookModel", lazy="subquery", back_populates="store"
    )
    def __str__(self):
        return f'{self.name}'
