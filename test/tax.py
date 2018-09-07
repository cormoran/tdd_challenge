import unittest
from tax import calc_price


class TestTax(unittest.TestCase):

    def test_calc_price(self):
        cases = [
            (24, [10, 12]),
            (62, [40, 16]),
            (160, [100, 45]),
            (171, [50, 50, 55]),
            (0, []),
        ]
        for expected, inputs in cases:
            self.assertEqual(expected, calc_price(inputs))
