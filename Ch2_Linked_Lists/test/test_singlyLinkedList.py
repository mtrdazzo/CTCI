from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import SinglyLinkedList, Empty
from unittest import TestCase


class TestSinglyLinkedList(TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()

    def tearDown(self):
        pass

    def test_is_empty(self):
        self.assertTrue(self.sll.is_empty())

    def test_add(self):
        for i in range(1, 11):
            self.sll.add(i)
            self.assertTrue(len(self.sll) == i)

    def test_remove(self):
        with self.assertRaises(Empty):
            self.sll.remove(1)

        for i in range(1, 11):
            self.sll.add(i)

        #Remove head of the list
        self.assertTrue(self.sll.remove(1) == 1)
        self.assertTrue(self.sll.head() == 2)

        #Remove the tail of the list
        self.assertTrue(self.sll.remove(10) == 10)
        self.assertTrue(self.sll.tail() == 9)

        #Remove middle node
        self.assertTrue(self.sll.remove(5) == 5)

        #Remove non-existent node
        self.assertIsNone(self.sll.remove(5))



