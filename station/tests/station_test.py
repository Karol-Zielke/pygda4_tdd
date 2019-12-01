import unittest
import datetime

from faker import Faker

from clock import Clock
from station.station import Station
from station.tests.time_table_stub import TimeTableStub
from time_table.time_table import TimeTable
import mock


class StationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.station = Station(Faker().word, {'d': TimeTableStub(tuple())})

    def tearDown(self) -> None:
        del self.station

    @mock.patch('time_table.time_table.TimeTable')
    def test_should_have_name(self, mock_time_table):
        mock_time_table.get_departure_times.return_value = (4234, '6576', 45645)

        station_name = Faker().word
        self.assertEqual(
            station_name,
            Station(station_name, {Faker().word: mock_time_table}).get_name(),
            msg=f'Should be {station_name}'
        )

    def test_should_know_actual_hour(self):
        self.assertEqual(
            datetime.datetime.now().strftime('%H:%M'),
            self.station.get_current_time()
        )

    def test_should_have_at_least_one_direction(self):
        self.assertGreaterEqual(
            len(Station(Faker().word, {'d': TimeTableStub(tuple())}).get_directions()),
            1,
            msg='Should have at least one direction'
        )

    def test_should_have_time_table_for_direction(self):
        self.assertIsInstance(
            Station(
                Faker().word,
                {'abc123': TimeTableStub(tuple())}
            ).time_tables['abc123'],
            TimeTable
        )

    def test_should_return_next_departure_time_depending_on_direction(self):
        station = Station(
                Faker().word,
                {'abc123': TimeTableStub(tuple())}
            )
        self.assertGreater(
            Clock.get_hour_in_seconds(
                station.get_next_departure_time('abc123')
            ),
            Clock.get_time()
        )

    def test_should_raise_error_for_unknown_direction(self):
        with self.assertRaises(ValueError):
            self.station.get_next_departure_time(Faker().word)
