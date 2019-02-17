from unittest import TestCase
from CTCI.Ch3_Stacks_and_Queues.common.common import Stack
from CTCI.Ch3_Stacks_and_Queues.exercises.CTCI_Ch3_Ex5 import sort_stack


class TestSortStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        pass

    def test_empty_stack(self):
        sort_stack(self.stack)
        # print(self.stack)

    def test_single_element_stack(self):
        self.stack.push(1)
        sort_stack(self.stack)
        # print(self.stack)

    def test_multiple_elements(self):
        self.stack.push(2)
        self.stack.push(1)

        # Correct order
        sort_stack(self.stack)
        # print(self.stack)

        # Incorrect order
        self.stack.push(0)
        sort_stack(self.stack)
        # print(self.stack)

        self.stack.push(8)
        sort_stack(self.stack)
        # print(self.stack)
