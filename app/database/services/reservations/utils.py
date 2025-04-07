from datetime import datetime, timedelta


class ReservationUtils:
    @staticmethod
    def is_cross(date_1: datetime, duration_1: int, date_2: datetime, duration_2: int) -> bool:
        end_1 = date_1 + timedelta(minutes=duration_1)
        end_2 = date_2 + timedelta(minutes=duration_2)

        return date_1 < end_2 and date_2 < end_1
