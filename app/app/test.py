from django.test import SimpleTestCase
from app import calc


class TestCalc(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(1, 6)
        self.assertEqual(res, 7)

    def test_subtract_number(self):
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)