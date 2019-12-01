from datetime import datetime

from hour.hour import Hour


class Clock:
    @staticmethod
    def get_time() -> int:
        now = datetime.now()
        return int(
            (now - now.replace(hour=0, minute=0, second=0, microsecond=0)
             ).total_seconds()
        )

    @staticmethod
    def get_formatted_time(seconds_since_midnight: int) -> str:
        hour, minutes = int(seconds_since_midnight / 3600), int(seconds_since_midnight % 3600 / 60)

        return '{hour}:{minutes}'.format(
            hour=hour if hour > 9 else f'0{hour}',
            minutes=minutes if minutes > 9 else f'0{minutes}'
        )

    @staticmethod
    def get_hour_in_seconds(formatted_hour: str) -> int:
        Hour(formatted_hour)
        hour, minutes = int(formatted_hour.split(':')[0]), int(formatted_hour.split(':')[1])
        return hour * 3600 + minutes * 60
