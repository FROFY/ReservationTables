from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.database.abstract_entities.abstract_base import Base


class Table(Base):
    name: Mapped[str]
    seats: Mapped[int]
    location: Mapped[str]

    reservations: Mapped[list["Reservation"]] = relationship(back_populates="tables")


class Reservation(Base):
    customer_name: Mapped[str]
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id", ondelete="cascade"))
    reservation_time: Mapped[datetime]
    duration_minutes: Mapped[int]

    tables: Mapped["Table"] = relationship(back_populates="reservations")

