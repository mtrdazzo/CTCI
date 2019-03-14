from unittest import TestCase
from CTCI.Ch8_Recursion_And_Dynamic_Programming.exercises.CTCI_Ch8_Ex2 import *


class TestFindOrigin(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_zero_grid(self):
        """Test grid size of zero"""
        self.assertTrue(to_bottom_right(0))
        self.assertTrue(to_bottom_right_memo(0))

    def test_empty_off_limits(self):
        """Test small and large data sets with no off limits"""
        self.assertTrue(to_bottom_right(5))
        self.assertTrue(to_bottom_right_memo(5))

        self.assertTrue(to_bottom_right(100))
        self.assertTrue(to_bottom_right_memo(100))

    def test_off_limits(self):
        """Test small and large data sets with bottom right off limits"""
        self.assertTrue(to_bottom_right(5, ((1, 1), (1, 0))))
        self.assertTrue(to_bottom_right_memo(5, ((1, 1), (1, 0))))
        self.assertTrue(to_bottom_right(30, ((1, 1), (1, 0))))
        self.assertTrue(to_bottom_right_memo(30, ((1, 1), (1, 0))))

    def test_no_path(self):
        """Test small and large data sets with bottom right totally off limits"""
        self.assertFalse(to_bottom_right(5, ((1, 1), (1, 0), (0, 1))))
        self.assertFalse(to_bottom_right_memo(5, ((1, 1), (1, 0), (0, 1))))

        self.assertFalse(to_bottom_right(11, ((1, 1), (1, 0), (0, 1))))
        self.assertFalse(to_bottom_right_memo(11, ((1, 1), (1, 0), (0, 1))))
