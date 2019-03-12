from unittest import TestCase
from CTCI.Ch8_Recursion_And_Dynamic_Programming.exercises.CTCI_Ch8_Ex3 import *


class TestBruteForce(TestCase):
    """Test Class to test brute force method of finding magic number"""
    def setUp(self):
        self.data = []

    def tearDown(self):
        pass

    def test_empty_list(self):
        """Empty list condition"""
        self.assertTrue(find_magic_number_brute_force(self.data) == -1)

    def test_list_no_magic_number(self):
        """List without magic number"""
        for num in range(1, 10, 2):
            self.data.append(num)
        self.assertTrue(find_magic_number_brute_force(self.data) == -1)

    def test_list_one_magic_number(self):
        """Single magic number in list"""
        for num in range(0, 10, 2):
            self.data.append(num)
        self.assertTrue(find_magic_number_brute_force(self.data) == 0)

    def test_list_multiple_magic_numbeR(self):
        """Greater than one magic number in list"""
        self.data.append(2)
        for num in range(1, 10):
            self.data.append(num)
        self.assertTrue(find_magic_number_brute_force(self.data) == 1)


class TestDistinct(TestCase):
    """Test class to test recursive approach for distinct values"""

    def setUp(self):
        self.data = []

    def tearDown(self):
        pass

    def test_empty_list(self):
        """Empty List data point"""
        self.assertTrue(find_magic_number_distinct(self.data) == -1)

    def test_no_magic_number(self):
        """No magic numbers in list"""
        for i in range(1, 10):
            self.data.append(i)
        self.assertTrue(find_magic_number_distinct(self.data) == -1)

    def test_single_magic_number(self):
        """No magic numbers in list"""
        self.data = [-1, 0, 1, 3]
        self.assertTrue(find_magic_number_distinct(self.data) == 3)

        self.data = [0, 2, 3]
        self.assertTrue(find_magic_number_distinct(self.data) == 0)

        self.data = [-1, 1, 3]
        self.assertTrue(find_magic_number_distinct(self.data) == 1)


class TestNonDistinct(TestCase):
    """Test class to test recursive approach for non-distinct values"""

    def setUp(self):
        self.data = []

    def tearDown(self):
        pass

    def test_empty_list(self):
        """Empty List data point"""
        self.assertTrue(find_magic_number_non_distinct(self.data) == -1)

    def test_no_magic_number(self):
        """No magic numbers in list"""
        for i in range(1, 10):
            self.data.append(i)
        self.assertTrue(find_magic_number_non_distinct(self.data) == -1)

    def test_single_magic_number(self):
        """No magic numbers in list"""
        self.data = [-1, 0, 2, 2]
        self.assertTrue(find_magic_number_non_distinct(self.data) == 2)

        self.data = [0, 2, 3]
        self.assertTrue(find_magic_number_non_distinct(self.data) == 0)

        self.data = [3, 3, 3, 3]
        self.assertTrue(find_magic_number_non_distinct(self.data) == 3)

        self.data = [0] * 10
        self.assertTrue(find_magic_number_non_distinct(self.data) == 0)
