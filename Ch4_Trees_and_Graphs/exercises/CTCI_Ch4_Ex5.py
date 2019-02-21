#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch4_Ex5.py
    Author:             Matt Randazzo
    Date created:       2/18/2019
    Date last modified: 2/18/2019
    Python Version:     3.7

    Description: CTCI 4.5 Validate BST

                Implement a function to check if a binary tree is a binary search tree

    Classes:

    Functions:

            is_bst
            is_bst_helper

"""


def is_bst(root):
    """Determine if binary tree is a binary search tree

    :param root Root of binary tree
    :return     True if binary tree is a binary search tree

    """

    def is_bst_helper(root, min, max):
        """Helper function to determine if binary tree is a BST

        :param root Root of binary tree
        :param min  Minimum value for root node
        :param max  Maximum value for root node
        :return     True if root has BST properties

        """
        if root is None:
            return True
        if max is not None and root.data > max:
            return False
        if min is not None and root.data <= min:
            return False

        left = is_bst_helper(root.left, min, root.data)
        right = is_bst_helper(root.right, root.data, max)

        return left and right

    # Empty Tree
    if root is None:
        return
    else:
        return is_bst_helper(root, None, None)
