from unittest import TestCase
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full
from CTCI.Ch3_Stacks_and_Queues.exercises.CTCI_Ch3_Ex2 import MinStack


class TestMinStack(TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def tearDown(self):
        pass

    def test_empty_stack(self):
        self.assertTrue(self.min_stack.is_empty())

        with self.assertRaises(Empty):
            self.min_stack.peek()

        with self.assertRaises(Empty):
            self.min_stack.pop()

        self.assertIsNone(self.min_stack.min())

    def test_single_element(self):

        self.min_stack.push(1)
        self.assertFalse(self.min_stack.is_empty())

        self.assertTrue(self.min_stack.min() == 1)
        self.assertTrue(self.min_stack.peek() == 1)
        self.assertTrue(self.min_stack.pop() == 1)

        self.assertTrue(self.min_stack.is_empty())

    def test_multiple_elements(self):

        self.min_stack.push(3)
        self.min_stack.push(2)
        self.min_stack.push(5)
        self.min_stack.push(3)

        self.assertTrue(self.min_stack.min() == 2)
        self.assertTrue(self.min_stack.peek() == 3)

        self.assertTrue(self.min_stack.pop() == 3)
        self.assertTrue(self.min_stack.peek() == 5)
        self.assertTrue(self.min_stack.min() == 2)

        self.assertTrue(self.min_stack.pop() == 5)
        self.assertTrue(self.min_stack.peek() == 2)

        self.assertTrue(self.min_stack.pop() == 2)
        self.assertTrue(self.min_stack.min() == 3)

    def test_full_stack(self):
        for i in range(20):
            self.min_stack.push(i + 1)

        with self.assertRaises(Full):
            self.min_stack.push(0)

