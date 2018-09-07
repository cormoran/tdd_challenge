import unittest
from tax import calc_price


class TestTax(unittest.TestCase):

    def test_calc_price(self):
        cases = [
            #
            (24, [10, 12]),
            (62, [40, 16]),
            (160, [100, 45]),
            (171, [50, 50, 55]),
            (0, []),
            # corner
            (0, [0]),
            (1100000, [1000000]),
            #
            (110, [1 for _ in range(100)]),
            (1100000 * 100, [1000000 for _ in range(100)]),
            # max (?) case
            (110000000000000, [1000000 for _ in range(100000000)]),
        ]
        for expected, inputs in cases:
            self.assertEqual(expected, calc_price(inputs))
