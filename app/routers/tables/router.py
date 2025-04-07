from fastapi import APIRouter, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.abstract_entities.session_maker import SessionDep
from app.database.schemas.schemas import SGetTable, SCreateTable, SPagination
from app.database.services.tables.dao import TableDAO

router = APIRouter(prefix="/tables", tags=["Tables"])


@router.post("")
async def create(table: SCreateTable, session: AsyncSession = SessionDep):
    await TableDAO.create_table(table, session)
    return "OK"


@router.get("", response_model=list[SGetTable])
async def get(pagination: SPagination = Query(), session: AsyncSession = SessionDep):
    return await TableDAO.get_with_pagination(pagination, session)


@router.delete("/{table_id}")
async def delete(table_id: int, session: AsyncSession = SessionDep) -> str:
    return await TableDAO.delete_row(table_id, session)
