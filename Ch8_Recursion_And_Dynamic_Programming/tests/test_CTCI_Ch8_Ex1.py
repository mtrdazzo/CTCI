from unittest import TestCase
from CTCI.Ch8_Recursion_And_Dynamic_Programming.exercises.CTCI_Ch8_Ex1 import *


class TestTripleStep(TestCase):
    """Test Recursive solution to three step problem"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_base_case(self):
        """Test base case condition of zero steps"""
        self.assertTrue(triple_step_combinations(0) == 1)

    def test_less_than_three_steps(self):
        """Values less than three steps"""
        self.assertTrue(triple_step_combinations(1) == 1)
        self.assertTrue(triple_step_combinations(2) == 2)

    def test_more_than_three_steps(self):
        """Values more than three steps"""
        self.assertTrue(triple_step_combinations(4) == 7)
        self.assertTrue(triple_step_combinations(5) == 13)


class TestMemoizedSolution(TestCase):
    """Test Recursive solution with memoized wrapper"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_base_case(self):
        """Test base case with zero steps left"""
        self.assertTrue(memoized_triple_step(0) == 1)

    def test_less_than_three_steps(self):
        """Test cases with less than three steps"""
        self.assertTrue(memoized_triple_step(1) == 1)
        self.assertTrue(memoized_triple_step(2) == 2)

    def test_greater_than_three_steps(self):
        """Test cases with greater than three steps"""
        self.assertTrue(memoized_triple_step(3) == 4)
        self.assertTrue(memoized_triple_step(4) == 7)
        self.assertTrue(memoized_triple_step(5) == 13)

