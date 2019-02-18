#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch4_Ex4.py
    Author:             Matt Randazzo
    Date created:       2/19/2019
    Date last modified: 2/19/2019
    Python Version:     3.7

    Description: CTCI 4.4 Check Balanced

                Implement a function to check if a binary tree is balanced. For the purposes of
                this question, a balanced tree is defined to be a tree such that the heights of
                the two subtrees of any node never differ by more than one.

    Classes:

            BalancedBST

    New Methods:

            is_balanced_first
            is_balanced
            _is_balanced_helper

"""
from CTCI.Ch4_Trees_and_Graphs.common.BinaryTree import BinarySearchTree


class BalancedBST(BinarySearchTree):

    def is_balanced(self):
        """Return True if BST is balanced

        :return BST balanced condition

        """
        if self.root is None:
            return
        return False if self._is_balanced_helper(self.root) is False else True

    def _is_balanced_helper(self, node):
        """BST Balance Helper

        :param node Root of BST
        :return     Height if balanced, False if unbalanced

        """
        if node is None:
            return -1

        left_height = self._is_balanced_helper(node.left)
        right_height = self._is_balanced_helper(node.right)

        if left_height is False or right_height is False:
            return False

        if abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height, right_height) + 1

    def is_balanced_first(self):
        """Determine if BST is balanced

        :returns If BST is balanced, return True

        """
        if self.is_empty():
            return

        if abs(self.get_height(self.root.left) - self.get_height(self.root.right)) > 1:
            return False
        else:
            return True
