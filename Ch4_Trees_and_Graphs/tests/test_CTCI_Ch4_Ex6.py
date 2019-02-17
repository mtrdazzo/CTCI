from unittest import TestCase
from CTCI.Ch4_Trees_and_Graphs.exercises.CTCI_Ch4_Ex6 import TreeParent


class TestFindSucessorNode(TestCase):

    def setUp(self):
        self.Tree = TreeParent()
        nodes = [5, 2, 1, 4, 7, 10, 8, 6]
        for node in nodes:
            self.Tree.add(node)

    def tearDown(self):
        pass

    def test_missing_node(self):
        self.assertIsNone(self.Tree.find_successor(11))

    def test_maximum_node(self):
        self.assertIsNone(self.Tree.find_successor(10))

    def test_with_right_node(self):
        self.assertTrue(self.Tree.find_successor(2).data == 4)

    def test_with_no_right_node(self):
        self.assertTrue(self.Tree.find_successor(4).data == 5)
        self.assertTrue(self.Tree.find_successor(6).data == 7)
