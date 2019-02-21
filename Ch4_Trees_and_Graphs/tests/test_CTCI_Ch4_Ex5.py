from unittest import TestCase
from CTCI.Ch4_Trees_and_Graphs.common.BinaryTree import BinarySearchTree, BinaryTree
from CTCI.Ch4_Trees_and_Graphs.exercises.CTCI_Ch4_Ex5 import is_bst
import random


class TestIsBST(TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bt = BinaryTree()

    def tearDown(self):
        pass

    def test_empty_tree(self):
        """Empty Tree, should return None"""
        self.assertIsNone(is_bst(self.bst.root))
        self.assertIsNone(is_bst(self.bt.root))

    def test_single_node_tree(self):
        """Test Tree with single root node with no children"""
        self.bst.add(1)
        self.bt.add(2)
        self.assertTrue(is_bst(self.bst.root))
        self.assertTrue(is_bst(self.bt.root))

    def test_multiple_nodes_greater_than_max(self):
        """Test Binary Tree with left node greater than max"""
        self.bt.add(1)
        self.bt.add(2)
        self.assertFalse(is_bst(self.bt.root))

    def test_multiple_nodes_less_than_min(self):
        """Test Binary Tree with right node less than min"""
        self.bt.add(5)
        self.bt.add(3)
        self.assertTrue(is_bst(self.bt.root))
        self.bt.add(4)
        self.assertFalse(is_bst(self.bt.root))

    def test_multiple_nodes_true(self):
        """Test BT with BST properties"""
        self.bt.add(5)
        self.bt.add(4)
        self.bt.add(6)
        self.bt.add(2)
        self.bt.add(5)

        self.assertTrue(is_bst(self.bt.root))

        for _ in range(10):
            self.bst.add(random.randint(0, 10))
        self.assertTrue(is_bst(self.bst.root))
