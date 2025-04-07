from datetime import datetime

from pydantic import BaseModel, Field


class SCreateTable(BaseModel):
    name: str = Field(description="Айди столика")
    seats: int = Field(gt=0, description="Количество мест")
    location: str = Field(description="Место столика в ресторане")


class SGetTable(SCreateTable):
    id: int = Field(description="Айди столика")


class SCreateReservation(BaseModel):
    customer_name: str = Field(description="Имя покупателя")
    table_id: int = Field(gt=0, description="ID столика")
    reservation_time: datetime = Field(description="Время брони")
    duration_minutes: int = Field(gt=0, description="Длительность сеанса")


class SGetReservation(SCreateReservation):
    id: int = Field(description="Айди брони")


class SPagination(BaseModel):
    page: int = Field(default=1, description="Текущая страница")
    page_size: int = Field(default=10, description="Размер страницы")
