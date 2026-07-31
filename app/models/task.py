from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    title: Mapped[str] = mapped_column(
        String(255),
        unique=False,
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        String(500),
        unique=False,
        nullable=True
    )

    user: Mapped["User"] = relationship(back_populates="tasks")
