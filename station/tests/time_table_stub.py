from hour import Hour
from time_table.time_table import TimeTable


class TimeTableStub(TimeTable):
    def __init__(self, departure_times: tuple):
        self.departure_times = (
            Hour('10:15'), Hour('12:10'), Hour('23:22')
        )
