#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch4_Ex3.py
    Author:             Matt Randazzo
    Date created:       2/19/2019
    Date last modified: 2/19/2019
    Python Version:     3.7

    Description: CTCI 4.3 List of Depth

                Given a binary tree, design a algorithm which creates a linked list of all
                the nodes at each depth (e.g., If you have a tree with depth D, you'll have
                D linked lists)

    Classes:

            None

    Functions:

            list_of_depths

"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import SinglyLinkedList


def list_of_depths(node, depth, linked_lists):
    """Create a linked list of all the nodes at each depth

    :param node          Root of binary tree
    :param depth         Depth of node
    :param linked_lists  List of linked lists

    """
    if node is None:
        return
    if len(linked_lists) == depth:
        new = SinglyLinkedList()
        new.add(node)
        linked_lists.append(new)
    else:
        linked_lists[depth].add(node)
    list_of_depths(node.left, depth + 1, linked_lists)
    list_of_depths(node.right, depth + 1, linked_lists)
