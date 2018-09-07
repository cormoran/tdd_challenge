import unittest
from tax import calc_price


class TestTax(unittest.TestCase):

    def test_calc_price(self):
        self.assertEqual(24, calc_price([10, 12]))
