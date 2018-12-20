import unittest
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex2 import KthLastSinglyLinkedList, Empty

class TestKthLastSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.sll = KthLastSinglyLinkedList()

    def tearDown(self):
        self.sll = None

    def test_empty_list(self):
        with self.assertRaises(Empty):
            self.sll.kth_to_last(1)

        with self.assertRaises(Empty):
            self.sll.kth_to_last_r(1)

    def test_single_element(self):
        self.sll.add(1)
        self.assertTrue(self.sll.kth_to_last(1) == 1)

        with self.assertRaises(ValueError):
            self.sll.kth_to_last(0)

        self.assertIsNone(self.sll.kth_to_last(2))

    def test_multiple_elements(self):
        for i in range(10):
            self.sll.add(i)
            self.assertTrue(self.sll.kth_to_last(1) == i)

        for i in range(1, 10):
            self.assertTrue(len(self.sll) - self.sll.kth_to_last(i) == i)

        self.assertIsNone(self.sll.kth_to_last(11))

    def test_recursive_kth(self):
        for i in range(10):
            self.sll.add(i)

        for i in range(1, 10):
            self.assertTrue(len(self.sll) - self.sll.kth_to_last_r(i) == i)

        self.assertIsNone(self.sll.kth_to_last_r(11))

