from hour import Hour

class TimeTable:
    def __init__(self, departure_times: tuple):
        seconds_in_day = 24 * 60 * 60
        for hour in departure_times:
            try:
                if hour.get_hour_in_seconds() > seconds_in_day:
                    raise ValueError('Too big value')
            except:
                raise ValueError('Incorrect Hour object')
        self.departure_times = departure_times

    def get_departure_times(self):
        return self.departure_times
