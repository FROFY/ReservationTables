from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.schemas.schemas import SPagination


class DAOController[T]:
    model: T

    @classmethod
    async def get_with_pagination(cls, pagination: SPagination, session: AsyncSession):
        try:
            query = select(cls.model)
            result = await session.execute(
                query.offset((pagination.page - 1) * pagination.page_size).limit(
                    pagination.page_size
                )
            )
            return result.scalars().all()
        except SQLAlchemyError as ex:
            logger.error(f"Ошибка при получении строки: {ex}")
            raise

    @classmethod
    async def delete_row(cls, row_id: int, session: AsyncSession):
        try:
            model_row = await session.get(cls.model, row_id)
            if model_row:
                await session.delete(model_row)
                await session.commit()
                return f"Row with ID {row_id} deleted"
            else:
                raise HTTPException(status_code=404, detail="Row not found")
        except SQLAlchemyError as ex:
            logger.error(f"Ошибка при удалении строки: {ex}")
            raise
