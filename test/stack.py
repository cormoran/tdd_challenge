import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_create(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push_and_top(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.top())

    def test_push_and_size(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.size())
        self.stack.push(2)
        self.assertEqual(2, self.stack.size())
