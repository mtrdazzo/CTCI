from unittest import TestCase
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full
from CTCI.Ch3_Stacks_and_Queues.exercises.CTCI_Ch3_Ex3 import SetOfStacks


class TestSetOfStacks(TestCase):
    def setUp(self):
        self.sos = SetOfStacks()

    def tearDown(self):
        pass

    def test_empty(self):
        with self.assertRaises(Empty):
            self.sos.pop()

        with self.assertRaises(Empty):
            self.sos.popAt(1)

    def test_single_stack(self):
        for i in range(5):
            self.sos.push(i)
        self.assertTrue(self.sos.peek() == 4)
        self.assertTrue(self.sos.pop() == 4)

        for i in range(6):
            self.sos.push(i)
        self.assertTrue(self.sos.peek() == 5)

        self.assertTrue(self.sos.pop() == 5)

        with self.assertRaises(IndexError):
            self.sos.popAt(2)

    def test_multiple_stack(self):
        for i in range(20):
            self.sos.push(i)
        self.sos.push(20)

        self.assertTrue(self.sos.popAt(1) == 9)

        self.assertTrue(self.sos.popAt(2) == 20)
        self.assertTrue(self.sos.peek() == 19)
