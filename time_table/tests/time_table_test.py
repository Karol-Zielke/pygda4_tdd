from unittest import TestCase
from random import randint
from hour.hour import Hour
from time_table.tests.hour_stub import HourStub
from time_table.time_table import TimeTable
import mock


class TimeTableTest(TestCase):
    # def setUp(self) -> None:
    #     self.time_table = TimeTable((2345, 4567, 8678))
    #
    # def tearDown(self) -> None:
    #     del self.time_table

    # def test_should_return_departure_times(self):
    #     self.assertNotEqual((), self.time_table.get_departure_times())
    #
    # def test_time_should_be_in_correct_format(self):
    #     time_index = randint(0, len(self.time_table.get_departure_times()) - 1)
    #     seconds_in_day = 24 * 60 * 60
    #     result_time = self.time_table.get_departure_times()[time_index]
    #
    #     self.assertTrue(
    #         type(result_time) is int,
    #         msg='Should be from Clock'
    #     )
    #     self.assertGreaterEqual(self.time_table.get_departure_times()[time_index], 0)
    #     self.assertLess(self.time_table.get_departure_times()[time_index], seconds_in_day)

    @mock.patch('hour.hour.Hour')
    def test_should_raise_error_for_too_big_values(self, hour_mock):
        hour_mock.get_hour_in_seconds.return_value = 574567567567

        with self.assertRaises(ValueError):
            TimeTable((hour_mock,))

    def test_should_raise_error_for_too_big_values_no_mock(self):
        hour = HourStub('11:15')

        with self.assertRaises(ValueError):
            TimeTable((hour,))

    def test_string_instead_hour(self):
        with self.assertRaises(ValueError):
            TimeTable(('bleble',))
