from unittest import TestCase
from CTCI.Ch4_Trees_and_Graphs.exercises.CTCI_Ch4_Ex4 import BalancedBST


class TestBSTBalanced(TestCase):

    def setUp(self):
        self.bst = BalancedBST()

    def tearDown(self):
        pass

    def test_empty_bst(self):
        """Test empty binary search tree"""
        self.assertIsNone(self.bst.is_balanced())

    def test_single_element(self):
        """Test single element bst"""
        self.bst.add(1)
        self.assertTrue(self.bst.is_balanced())

    def test_balanced(self):
        """Test balanced bst"""
        nodes = [5, 7, 6, 2, 3, 4, 0, 9, 8, 10, 1]
        for node in nodes:
            self.bst.add(node)
        self.assertTrue(self.bst.is_balanced())

    def test_unbalanced_left_tree(self):
        """Test unbalanced left tree"""
        nodes = [5, 7, 6, 2, 3, 4, 0, 9, 8, 10, 1, 0, 0, 0]
        for node in nodes:
            self.bst.add(node)
        self.assertFalse(self.bst.is_balanced())

    def test_unbalanced_right_tree(self):
        """test unbalanced right tree"""
        nodes = [5, 7, 6, 2, 3, 4, 0, 9, 8, 10, 1, 11]
        for node in nodes:
            self.bst.add(node)
        self.assertFalse(self.bst.is_balanced())
