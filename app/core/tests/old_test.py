from django.test import TestCase

from example.calc import sub2


class CalcTests(TestCase):

    # always start with 'test'[]
    def test_subtract_numbers(self):
        """ test that values are subtracted and returned"""
        self.assertEqual(sub2(7, 11), 4)
