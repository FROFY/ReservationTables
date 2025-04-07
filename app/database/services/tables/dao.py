from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.abstract_entities.dao_base import DAOController
from app.database.models.models import Table
from app.database.schemas.schemas import SCreateTable


class TableDAO(DAOController[Table]):
    model = Table

    @classmethod
    async def create_table(cls, table: SCreateTable, session: AsyncSession):
        table_model = table.model_dump()
        try:
            session.add(cls.model(**table_model))
            await session.commit()
        except SQLAlchemyError as ex:
            logger.error(f"Ошибка при создании столика: {ex}")
            raise
