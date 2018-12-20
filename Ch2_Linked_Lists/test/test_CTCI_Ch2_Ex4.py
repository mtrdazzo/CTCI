from unittest import TestCase
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex4 import PartitionSinglyLinkedList, Empty


class TestPartitionSinglyLinkedList(TestCase):

    def setUp(self):
        self.pll = PartitionSinglyLinkedList()

    def test_partition_empty(self):
        with self.assertRaises(Empty):
            self.pll.partition(5)

    def test_partition_single_element(self):
        self.pll.add(1)

        # Partition list with single element
        self.pll.partition(1)
        self.assertTrue(self.pll.head() == 1
                        and self.pll.tail() == 1)

        # Partition list with single element, value not in list
        self.assertIsNone(self.pll.partition(2))

    def test_partition_multiple_elements(self):
        self.pll.add(1)
        self.pll.add(2)

        # Partition list with single element
        self.pll.partition(2)
        self.assertTrue(self.pll.head() == 1
                        and self.pll.tail() == 2)

        # Partition list with single element, value not in list
        self.assertIsNone(self.pll.partition(3))

        elements = [3, 1, 5, 2, 8, 9, 10, 4]

        for e in elements:
            self.pll.add(e)

        # Partition value with elements in both partitions
        self.pll.partition(4)

        # Partition value with no elements less than
        self.pll.partition(1)

        # Partition value with only one element greater than or equal
        self.pll.partition(10)

