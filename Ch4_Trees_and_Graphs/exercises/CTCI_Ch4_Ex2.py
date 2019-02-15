#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch4_Ex2.py
    Author:             Matt Randazzo
    Date created:       2/15/2019
    Date last modified: 2/15/2019
    Python Version:     3.7

    Description: CTCI 4.2 Minimal Tree
                 Given a sorted (increasing order) array with unique integer elements,
                 write an algorithm to create a binary search tree with minimal height.

    Classes:

            None

    Functions:

            create_min_tree
            create_min_tree_helper

"""
from CTCI.Ch4_Trees_and_Graphs.common.BinaryTree import Tree


def create_min_tree(arr):
    """Create minimum binary tree given array

    :param arr List of node keys

    """

    def create_min_tree_helper(tree, array, min, max):
        """Recursive function to add middle element to tree

        :param tree  binary search tree data structure
        :param array list of node keys
        :param min   minimum array index
        :param max   maximum array index

        :return Binary Tree with minimum height

        """
        if min > max:
            return

        middle = (max + min) // 2
        tree.add(array[middle])

        create_min_tree_helper(tree, array, min, middle - 1)
        create_min_tree_helper(tree, array, middle + 1, max)

    if arr is None:
        return

    min_tree = Tree()
    create_min_tree_helper(min_tree, arr, 0, len(min_tree) - 1)

    return min_tree
