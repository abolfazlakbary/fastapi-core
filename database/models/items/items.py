from core.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String


class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)