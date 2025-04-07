from fastapi import APIRouter, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.abstract_entities.session_maker import SessionDep
from app.database.schemas.schemas import (
    SCreateReservation,
    SGetReservation,
    SPagination,
)
from app.database.services.reservations.dao import ReservationDAO

router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.post("")
async def create(reservation: SCreateReservation, session: AsyncSession = SessionDep):
    await ReservationDAO.create_reservation(reservation, session)
    return "OK"


@router.get("", response_model=list[SGetReservation])
async def get(pagination: SPagination = Query(), session: AsyncSession = SessionDep):
    return await ReservationDAO.get_with_pagination(pagination, session)


@router.delete("/{reservation_id}")
async def delete(reservation_id: int, session: AsyncSession = SessionDep) -> str:
    return await ReservationDAO.delete_row(reservation_id, session)
