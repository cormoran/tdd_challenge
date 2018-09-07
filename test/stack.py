import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_create(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
