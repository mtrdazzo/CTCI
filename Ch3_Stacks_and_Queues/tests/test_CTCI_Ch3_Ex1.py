from unittest import TestCase
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full
from CTCI.Ch3_Stacks_and_Queues.exercises.CTCI_Ch3_Ex1 import ThreeInOneStack


class TestThreeInOneStack(TestCase):
    def setUp(self):
        self.stack = ThreeInOneStack()

    def tearDown(self):
        pass

    def test_empty_stack(self):
        # Verify each is empty
        for s in range(ThreeInOneStack.NUMBER_OF_STACKS):
            self.assertTrue(self.stack.stacks[s - 1].is_empty())

        # Pop each empty stack
        for s in range(1, ThreeInOneStack.NUMBER_OF_STACKS + 1):
            with self.assertRaises(Empty):
                self.stack.pop(s)

        # Peek each empty stack
        for s in range(1, ThreeInOneStack.NUMBER_OF_STACKS + 1):
            with self.assertRaises(Empty):
                self.stack.peek(s)

        # Verify each stack is not full
        for s in range(ThreeInOneStack.NUMBER_OF_STACKS):
            self.assertFalse(self.stack.stacks[s - 1].is_full())

    def test_single_element_stack(self):
        # Verify each is empty
        for s in range(ThreeInOneStack.NUMBER_OF_STACKS):
            self.assertTrue(self.stack.stacks[s - 1].is_empty())

        # Push element 1 to each empty stack
        for s in range(1, ThreeInOneStack.NUMBER_OF_STACKS + 1):
            self.stack.push(1, s)

        # Verify each is no longer empty
        for s in range(ThreeInOneStack.NUMBER_OF_STACKS):
            self.assertFalse(self.stack.stacks[s - 1].is_empty())
            self.assertTrue(self.stack.peek(s + 1) == 1)

        # Pop element from each stack
        for s in range(1, ThreeInOneStack.NUMBER_OF_STACKS + 1):
            self.assertTrue(self.stack.pop(s) == 1)

        # Verify each is empty
        for s in range(ThreeInOneStack.NUMBER_OF_STACKS):
            self.assertTrue(self.stack.stacks[s - 1].is_empty())

    def test_multiple_element_stack(self):
        for s in range(1, ThreeInOneStack.NUMBER_OF_STACKS + 1):
            for e in range(10):
                self.stack.push(e, s)
                self.assertTrue(self.stack.peek(s) == e)

            with self.assertRaises(Full):
                self.stack.push(0, s)

            for e in range(9, -1, -1):
                self.assertTrue(self.stack.pop(s) == e)

            with self.assertRaises(Empty):
                self.stack.pop(s)

            with self.assertRaises(Empty):
                self.stack.peek(s)
