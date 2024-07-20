from core.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger, ForeignKey


class UserItem(Base):
    __tablename__ = "user_items"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    item_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("items.id"), nullable=False)