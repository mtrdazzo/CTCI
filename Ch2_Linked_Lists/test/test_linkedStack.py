from unittest import TestCase
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import LinkedStack, Empty


class TestLinkedStack(TestCase):

    def setUp(self):
        self.ls = LinkedStack()

    def test_is_empty(self):
        with self.assertRaises(Empty):
            self.ls.pop()

        with self.assertRaises(Empty):
            self.ls.top()

        self.ls.push(1)

        self.assertFalse(self.ls.is_empty())

    def test_push(self):
        self.ls.push(1)
        self.assertTrue(self.ls.top() == 1)

        self.ls.push(2)
        self.assertTrue(self.ls.top() == 2)

    def test_pop(self):
        self.ls.push(1)
        self.assertTrue(self.ls.pop() == 1)

        self.ls.push(1)
        self.ls.push(2)
        self.assertTrue(self.ls.pop() == 2)
