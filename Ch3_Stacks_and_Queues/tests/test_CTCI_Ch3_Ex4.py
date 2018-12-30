from unittest import TestCase
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full, Stack
from CTCI.Ch3_Stacks_and_Queues.exercises.CTCI_Ch3_Ex4 import MyQueue


class TestMyQueue(TestCase):

    def setUp(self):
        self.mq = MyQueue()

    def tearDown(self):
        pass

    def test_empty(self):
        with self.assertRaises(Empty):
            self.mq.dequeue()

        with self.assertRaises(Empty):
            self.mq.front()

        self.assertTrue(self.mq.is_empty())

    def test_single_element(self):
        self.mq.enqueue(1)
        self.assertFalse(self.mq.is_empty())

        self.assertTrue(self.mq.dequeue() == 1)
        self.assertTrue(self.mq.is_empty())

    def test_multiple_elements(self):
        for i in range(20):
            self.mq.enqueue(i)

        with self.assertRaises(Full):
            self.mq.enqueue(1)

        for i in range(20):
            self.assertTrue(self.mq.dequeue() == i)
