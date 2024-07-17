from core.database.connection import Base
from sqlalchemy import INTEGER, String
from sqlalchemy.orm import Mapped, mapped_column

class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)