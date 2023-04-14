from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base_class import Base


class CategoryRequest(Base):
    name: Mapped[str] = mapped_column(
        String
    )
    description: Mapped[str] = mapped_column(
        String
    )
    status: Mapped[str] = mapped_column(
        String
    )
    store_owner_id: Mapped[str] = mapped_column(
        String
    )
    def __str__(self):
        return f'{self.name}{self.status}'