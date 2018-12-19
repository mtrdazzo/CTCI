from unittest import TestCase
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Node, Empty
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex3 import delete_middle_node


class TestDeleteMiddleNode(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_node(self):
        """Delete node in empty linked list, raise Empty"""
        with self.assertRaises(Empty):
            delete_middle_node(None)

    def test_single_node(self):
        """Delete node with one element in linked list, raise IndexError"""
        node = Node(1)

        with self.assertRaises(IndexError):
            delete_middle_node(node)

    def test_two_nodes(self):
        """Deletes head node in linked list with two elements"""
        node = Node(1)
        node.next = Node(2)

        delete_middle_node(node)
        self.assertIsNone(node.next)
        self.assertTrue(node.data == 2)

    def test_more_two_nodes(self):
        """Delete middle node in linked list of length > two elements"""
        node = Node(1)
        node.next = Node(3)
        node.next.next = Node(4)

        delete_middle_node(node.next)
        self.assertTrue(node.next.data == 4)
