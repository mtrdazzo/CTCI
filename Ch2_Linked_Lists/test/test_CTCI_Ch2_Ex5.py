import unittest
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex5 import *


class TestSumLinkedList(unittest.TestCase):

    def setUp(self):
        self.sll = SumSinglyLinkedList()

    def tearDown(self):
        pass

    def test_add_empty_lists(self):
        self.assertIsNone(self.sll.sum_linked_lists(SumSinglyLinkedList()))

    def test_add_single_linked_list(self):
        for i in range(3):
            self.sll.add(i)
        sll2 = SumSinglyLinkedList()

        # Adding 210 and Empty
        self.assertTrue(self.sll.sum_linked_lists(sll2).nodes_to_int() == "210")

        # Adding Empty and 210
        self.assertTrue(sll2.sum_linked_lists(self.sll).nodes_to_int() == "210")

    def test_different_sizes(self):
        sll2 = SumSinglyLinkedList()
        for i in range(3):
            self.sll.add(i)
        sll2.add(9)

        # Adding 210 and 9
        self.assertTrue(self.sll.sum_linked_lists(sll2).nodes_to_int() == "219")

        # Adding 9 and 210
        self.assertTrue(sll2.sum_linked_lists(self.sll).nodes_to_int() == "219")

    def test_add_lists_no_carry(self):
        sll2 = SumSinglyLinkedList()
        for i in range(3):
            self.sll.add(i)
            sll2.add(i)

        # Adding 210 and 210
        self.assertTrue(self.sll.sum_linked_lists(sll2).nodes_to_int() == "420")

    def test_add_lists_carry_middle(self):
        sll2 = SumSinglyLinkedList()
        for i in range(3):
            self.sll.add(i)
        sll2.add(0)
        sll2.add(9)

        # Adding 210 and 90
        self.assertTrue(self.sll.sum_linked_lists(sll2).nodes_to_int() == "300")

    def test_add_lists_carry_front(self):
        sll2 = SumSinglyLinkedList()

        for i in range(3):
            self.sll.add(i)
        sll2.add(0)
        sll2.add(0)
        sll2.add(8)

        # Adding 210 and 800
        self.assertTrue(self.sll.sum_linked_lists(sll2).nodes_to_int() == "1010")


class TestSumLinkedLists(unittest.TestCase):

    def setUp(self):
        # Linked list 0->1->2 or 210
        self.sll1 = Node(0)
        self.sll1.next = Node(1)
        self.sll1.next.next = Node(2)

    def tearDown(self):
        None

    def test_empty_nodes(self):
        # Adding None and None
        self.assertIsNone(None, None)

    def test_single_empty(self):
        # Adding None and 210
        sum = sum_linked_lists(None, self.sll1)
        self.assertTrue(nodes_to_int(sum) == "210")

        # Adding 210 and None
        sum = sum_linked_lists(self.sll1, None)
        self.assertTrue(nodes_to_int(sum) == "210")

    def test_no_carry(self):
        # Different sizes
        sll2 = Node(3)

        # Adding 210 and 3
        sum = sum_linked_lists(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum) == "213")

        # Adding 3 and 210
        sum = sum_linked_lists(sll2, self.sll1)
        self.assertTrue(nodes_to_int(sum) == "213")

        # Same size lists
        sll2.next = Node(1)
        sll2.next.next = Node(3)

        # Adding 210 and 313
        sum = sum_linked_lists(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum) == "523")

        # Adding 313 and 210
        sum = sum_linked_lists(sll2, self.sll1)
        self.assertTrue(nodes_to_int(sum) == "523")

    def test_carry(self):
        # Different Sizes
        sll2 = Node(1)
        sll2.next = Node(9)

        # Adding 210 and 91
        sum = sum_linked_lists(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum) == "301")

        # Adding 91 and 210
        sum = sum_linked_lists(sll2, self.sll1)
        self.assertTrue(nodes_to_int(sum) == "301")

    def test_carry_node_font(self):
        sll2 = Node(0)
        sll2.next = Node(0)
        sll2.next.next = Node(8)

        # Adding 210 and 800
        sum = sum_linked_lists(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum) == "1010")

class TestSumLinkedListReverse(unittest.TestCase):

    def setUp(self):
        # Linked list 1->2->3 or 123
        self.sll1 = Node(1)
        self.sll1.next = Node(2)
        self.sll1.next.next = Node(3)

    def tearDown(self):
        pass

    def test_add_empty_nodes(self):
        self.assertIsNone(sum_linked_lists_reverse(None, None))

    def test_add_single_empty_node(self):
        # Adding 123 and None
        sum = sum_linked_lists_reverse(self.sll1, None)
        self.assertTrue(nodes_to_int(sum, False) == "123")

        # Adding None and 123
        sum = sum_linked_lists_reverse(None, self.sll1)
        self.assertTrue(nodes_to_int(sum, False) == "123")

    def test_no_carry(self):
        # Different Sizes
        sll2 = Node(5)

        # Adding 123 and 5
        sum = sum_linked_lists_reverse(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum, False) == "128")

        # Adding 5 and 123
        sum = sum_linked_lists_reverse(sll2, self.sll1)
        self.assertTrue(nodes_to_int(sum, False) == "128")

        # Adding linked lists of same size
        sll2.next = Node(3)
        sll2.next.next = Node(6)

        # Adding 123 and 536
        sum = sum_linked_lists_reverse(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum, False) == "659")

        # Adding 536 and 123
        sum = sum_linked_lists_reverse(sll2, self.sll1)
        self.assertTrue(nodes_to_int(sum, False) == "659")

    def test_carry(self):
        sll2 = Node(9)

        # Adding 123 and 9
        sum = sum_linked_lists_reverse(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum, False) == "132")

        # Adding 9 and 123
        sum = sum_linked_lists_reverse(sll2, self.sll1)
        self.assertTrue(nodes_to_int(sum, False) == "132")

        sll2.next = Node(0)
        sll2.next.next = Node(0)

        # Adding 123 and 900
        sum = sum_linked_lists_reverse(self.sll1, sll2)
        self.assertTrue(nodes_to_int(sum, False) == "1023")


unittest.main()

