from unittest import TestCase
from CTCI.Ch4_Trees_and_Graphs.exercises.CTCI_Ch4_Ex2 import create_min_tree


class TestCreateMinTree(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_list(self):
        """Test Empty List"""
        empty_list = []
        empty_tree = create_min_tree(empty_list)

        self.assertTrue(empty_tree.is_empty())
        self.assertTrue(empty_tree.root is None)

    def test_none_type(self):
        """Test passing None to create min tree"""
        none_tree = create_min_tree(None)
        self.assertIsNone(none_tree)

    def test_single_element(self):
        """Test passing list with a single element"""
        single_element_list =[2]
        single_tree = create_min_tree(single_element_list)
        self.assertTrue(len(single_tree) == 1)
        self.assertTrue(single_tree.root.data == 2)

    def test_two_elements(self):
        """Test passing list with two elements"""
        two_elements = [1, 4]
        two_element_tree = create_min_tree(two_elements)
        self.assertTrue(len(two_element_tree) == 2)
        self.assertTrue(two_element_tree.root.data == 1)

    def test_odd_number_elements(self):
        """Test passing list with an odd number of elements"""
        arr = [i for i in range(1, 10)]
        odd_element_tree = create_min_tree(arr)
        self.assertTrue(len(odd_element_tree) == 9)
        self.assertTrue(odd_element_tree.root.data == 5)

    def test_even_number_elements(self):
        """test passing list with an even number of elements"""
        arr = [i for i in range(1, 11)]
        even_element_tree = create_min_tree(arr)
        self.assertTrue(len(even_element_tree) == 10)
        self.assertTrue(even_element_tree.root.data == 5)
