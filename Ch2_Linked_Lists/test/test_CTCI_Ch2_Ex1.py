from unittest import TestCase
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Empty
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex1 import RemoveDupsSinglyLinkedList


class TestRemoveDupsSinglyLinkedList(TestCase):

    def setUp(self):
        self.sll = RemoveDupsSinglyLinkedList()

    def test_remove_dups_empty(self):

        with self.assertRaises(Empty):
            self.sll.remove_dups_iterative()

    def test_remove_no_dupes(self):

        for i in range(10):
            self.sll.add(i)
        prev_len = len(self.sll)
        self.sll.remove_dups_iterative()
        self.assertTrue(len(self.sll) == prev_len)

    def test_single_dupe_front(self):
        self.sll.add(1)
        self.sll.add(1)

        prev_len = len(self.sll)
        self.sll.remove_dups_iterative()
        self.assertTrue(len(self.sll) == prev_len - 1)

    def test_single_dupe_back(self):
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(1)

        self.sll.remove_dups_iterative()
        self.assertTrue(self.sll.tail() == 2)

    def test_single_dupe_consecutive(self):
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(1)
        self.sll.add(1)

        self.sll.remove_dups_iterative()
        self.assertTrue(self.sll.tail() == 2)

    def test_single_dupe_inside(self):
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(3)
        self.sll.add(2)

        self.sll.remove_dups_iterative()
        self.assertTrue(self.sll.tail() == 3)

    def test_single_dupe_inside_consecutive(self):
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(3)
        self.sll.add(2)
        self.sll.add(2)

        self.sll.remove_dups_iterative()
        self.assertTrue(self.sll.tail() == 3)

    def test_single_dupe_tail(self):
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(2)
        self.sll.add(2)

        self.sll.remove_dups_iterative()
        self.assertTrue(len(self.sll) == 2)

    def test_remove_multiple_dupes(self):
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(1)
        self.sll.add(2)
        self.sll.add(1)
        self.sll.add(3)
        self.sll.add(3)
        self.sll.add(3)
        self.sll.add(3)
        self.sll.add(3)
        self.sll.add(4)

        self.sll.remove_dups_iterative()
        self.assertTrue(len(self.sll) == 4)
