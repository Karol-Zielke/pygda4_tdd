from datetime import datetime

from clock import Clock


class Station:
    def __init__(self, station_name, directions: dict):
        self.station_name = station_name
        self.directions = directions.keys()
        self.time_tables = directions

    def get_name(self):
        return self.station_name

    def get_current_time(self):
        return datetime.now().strftime('%H:%M')

    def get_directions(self):
        return self.directions

    def get_next_departure_time(self, direction) -> str:
        if direction not in self.directions:
            raise ValueError('Unknown direction')

        current_time = Clock.get_time()
        for hour in self.time_tables[direction].get_departure_times():
            if hour.get_hour_in_seconds() > current_time:
                return Clock.get_formatted_time(hour.get_hour_in_seconds())

        return Clock.get_formatted_time(
            self.time_tables[direction].get_departure_times()[0]
        )
