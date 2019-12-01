import unittest

from clock import Clock
from datetime import datetime


class ClockTest(unittest.TestCase):
    def test_result(self):
        now = datetime.now()
        seconds_since_midnight = (
                now - now.replace(hour=0, minute=0, second=0, microsecond=0)
        ).total_seconds()

        self.assertEqual(
            int(seconds_since_midnight),
            Clock.get_time(),
            msg='should return current value of seconds from midnight in integer'
        )

    def test_should_return_formatted_hour(self):
        now = datetime.now()
        seconds_since_midnight = int(
            (now - now.replace(hour=0, minute=0, second=0, microsecond=0)
            ).total_seconds()
        )

        hour, minutes = int(seconds_since_midnight / 3600), int(seconds_since_midnight % 3600 / 60)

        expected = '{hour}:{minutes}'.format(
            hour=hour if hour > 9 else f'0{hour}',
            minutes=minutes if minutes > 9 else f'0{minutes}'
        )
        self.assertEqual(expected, Clock.get_formatted_time(seconds_since_midnight))
