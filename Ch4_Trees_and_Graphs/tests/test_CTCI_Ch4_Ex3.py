from unittest import TestCase
from CTCI.Ch4_Trees_and_Graphs.common.BinaryTree import Tree
from CTCI.Ch4_Trees_and_Graphs.exercises.CTCI_Ch4_Ex3 import list_of_depths


class TestLinkedListLevel(TestCase):
    def setUp(self):
        self.linked_lists = []
        self.tree = Tree()

    def tearDown(self):
        pass

    def test_empty_tree(self):
        """Test passing empty tree"""
        list_of_depths(self.tree.root, 0, self.linked_lists)
        self.assertTrue(len(self.linked_lists) == 0)

    def test_single_depth(self):
        """Test passing single node"""
        self.tree.add(1)
        list_of_depths(self.tree.root, 0, self.linked_lists)
        self.assertTrue(len(self.linked_lists) == 1)

    def test_multiple_depth(self):
        """Test passing multiple nodes with multiple levels"""
        nodes = [5, 7, 6, 2, 3, 4, 0, 9, 8, 10, 1]
        for node in nodes:
            self.tree.add(node)
        list_of_depths(self.tree.root, 0, self.linked_lists)
        self.assertTrue(len(self.linked_lists) == 4)


