from datetime import datetime
from typing import Dict, Any, Annotated

from app.config import database_url
from sqlalchemy import func, TIMESTAMP, Integer
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

engine = create_async_engine(url=database_url)
async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
unique_str = Annotated[str, mapped_column(unique=True, nullable=False)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, sort_order=-1
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )

    @declared_attr
    def __tablename__(cls) -> str:
        # CamelCase → snake_case
        name = cls.__name__[0].lower() + cls.__name__[1:]
        name = "".join(["_" + c.lower() if c.isupper() else c for c in name]).lstrip(
            "_"
        )

        if name.endswith(("s", "x", "z", "ch", "sh")):
            return name + "es"
        elif name.endswith("y"):
            return name[:-1] + "ies"
        else:
            return name if name.endswith("s") else name + "s"

    def to_dict(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        """Строковое представление объекта для удобства отладки."""
        return f"<{self.__class__.__name__}(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})>"
