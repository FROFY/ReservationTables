from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.abstract_entities.dao_base import DAOController
from app.database.models.models import Table, Reservation
from app.database.schemas.schemas import SCreateReservation
from app.database.services.reservations.utils import ReservationUtils


class ReservationDAO(DAOController[Reservation]):
    model = Reservation

    @classmethod
    async def create_reservation(
        cls, reservation: SCreateReservation, session: AsyncSession
    ):
        reservation_model = reservation.model_dump()
        try:
            table = await session.execute(
                select(Table).where(Table.id == reservation_model["table_id"])
            )
            if table.scalar_one_or_none() is None:
                raise HTTPException(status_code=404, detail="Table not found")
            reservations = await session.execute(select(cls.model))
            reservations = reservations.scalars().all()
            if reservations:
                for reserve in reservations:
                    if ReservationUtils.is_cross(
                        reserve.reservation_time,
                        reserve.duration_minutes,
                        reservation_model["reservation_time"],
                        reservation_model["duration_minutes"],
                    ):
                        raise HTTPException(status_code=409, detail="Table is busy")
            session.add(Reservation(**reservation_model))
            await session.commit()
        except SQLAlchemyError as ex:
            logger.error(f"Ошибка при создании бронирования: {ex}")
            raise
