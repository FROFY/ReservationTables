import datetime

from app.database.services.reservations.utils import ReservationUtils


def test_cross_dates():
    """
    Проверка корректности определения пересечения дат бронирования.
    """
    date1 = datetime.datetime.now()
    duration1 = 30

    date2 = datetime.datetime.now() + datetime.timedelta(minutes=30)
    duration2 = 10

    assert ReservationUtils.is_cross(date1, duration1, date2, duration2) is False

    date1 = datetime.datetime.now()
    duration1 = 60

    date2 = datetime.datetime.now() + datetime.timedelta(minutes=30)
    duration2 = 10
    assert ReservationUtils.is_cross(date1, duration1, date2, duration2) is True
