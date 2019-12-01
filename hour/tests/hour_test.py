# -*- coding: utf-8 -*-
import unittest

import faker as faker

from hour import Hour, HourError
from unittest_dataprovider import data_provider


class HourTest(unittest.TestCase):
    # sposób 1
    incorrect_hours = lambda: (
        ('11.05',), ('ef.gh',), ('24:11',), ('23:60',), ('1:30',), ('-1:11',),
        ('23:-8',), (' 1:30',), ('001:30',), ('01:030',), ('11: 5',), ('  :11', )
    )

    # sposób 2 :P (specjalnie dla Rafała B.)
    @staticmethod
    def incorrect_values():
        return (
            ('11.05',), ('ef.gh',), ('24:11',), ('23:60',), ('1:30',), ('-1:11',),
            ('23:-8',), (' 1:30',), ('001:30',), ('01:030',), ('11: 5',)
        )

    # @data_provider(incorrect_values) :P
    @data_provider(incorrect_hours)
    def test_raise_error(self, hour_value):
        """Raises error with incorrect hour values"""
        with self.assertRaises(HourError):
            Hour(hour_value)

    def test_should_work_with_correct_data(self):
        """Podajemy prawdziwą godzinę i sprawdzamy, czy działa"""
        correct_hour = faker.Faker().time(pattern="%H:%M")
        hour = Hour(correct_hour)
        actual_hour = hour.get_hour()

        self.assertEqual(correct_hour, actual_hour)
