import unittest
import subprocess
from calc_price import calc_price_stream
import io


class TestCalcPrice(unittest.TestCase):
    def test_stream_input(self):
        cases = [
            ("\n".join(
                ["10,12", "40,16", "100,45", "", "50,50,55"]) + "\n",
             "\n".join(["24", "62", "160", "0", "171"]) + "\n"),
            ("\n", "\n"),
            ("\n\n", "0\n"),
            ("\n\n\n", "0\n0\n"),
            ("\n100\n", "0\n110\n")
        ]

        for input, expected in cases:
            output = io.StringIO()
            input_file = io.StringIO(input)
            expected_file = io.StringIO(expected)
            calc_price_stream(fin=input_file, fout=output)

            self.assertEqual(output.getvalue(),
                             expected_file.read())
