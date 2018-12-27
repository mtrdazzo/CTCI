from unittest import TestCase
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex7 import is_intersection
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Node

class TestIsIntersection(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_linked_lists(self):
        self.assertFalse(is_intersection(None, None))

    def test_single_empty_linked_list(self):
        ll_a = Node(1)

        self.assertFalse(is_intersection(ll_a, None))
        self.assertFalse(is_intersection(None, ll_a))

    def test_linked_list_intersection_single_element(self):
        ll_a = Node(1)
        ll_b = Node(2)
        self.assertTrue(is_intersection(ll_a, ll_a) is ll_a)
        self.assertFalse(is_intersection(ll_a, ll_b))

    def test_linked_list_greater_one_element(self):
        ll_a = Node(1)
        ll_a.next = Node(3)
        ll_a.next.next = Node(4)

        ll_b = Node(0)
        ll_b.next = ll_a.next.next

        # Same Node
        self.assertTrue(is_intersection(ll_a, ll_a) == ll_a)

        # Last Node, different sizes
        self.assertTrue(is_intersection(ll_a, ll_b) == ll_b.next)

        # Last Node, same sizes
        ll_b.next = Node(4)
        ll_b.next.next = ll_a.next.next
        self.assertTrue(is_intersection(ll_a, ll_b) == ll_b.next.next)

