import unittest
from validate_addr import validate_addr, validate_domain, validate_quated_string


class TestValidateAddr(unittest.TestCase):

    def test_validate_addr(self):
        ok_cases = [
            "abc@example.com",
        ]
        ng_cases = [
            "a..bc@example.com",
        ]
        for case in ok_cases:
            self.assertTrue(validate_addr(case))
        for case in ng_cases:
            self.assertFalse(validate_addr(case))

    def test_validate_domain(self):
        ok_cases = [
            "example.com",
            #
            "!#$%&'*+-/=?^_`{|}~.a",  # D1
        ]
        ng_cases = [
            "",  # D5
            "aa..aa",  # D4
            "aa.",  # D3
            ".aa",  # D2
            "@",  # D1
            #
            "."
        ]
        for case in ok_cases:
            self.assertTrue(validate_domain(case))
        for case in ng_cases:
            self.assertFalse(validate_domain(case))

    def test_validate_quated_string(self):
        ok_cases = [
            '"abc"',
            '"ab\\"c"',  # LQ4
            '"ab\\\\c"',  # LQ4
        ]
        ng_cases = [
            'aaa"',  # LO1
            '"aaa',  # LQ2
            '"😄"',  # LQ3
            '"',  # LQ5
            '"ab"c"',  # LQ4
            '"ab\\c"',# LQ4
        ]
        for case in ok_cases:
            self.assertTrue(validate_quated_string(case), case)
        for case in ng_cases:
            self.assertFalse(validate_quated_string(case), case)
