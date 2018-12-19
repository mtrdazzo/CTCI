#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex3.py
    Author:             Matt Randazzo
    Date created:       12/19/2018
    Date last modified: 12/19/2018
    Python Version:     3.7

    Description: CTCI 2.3 Delete Middle Node
                 Implement an algorithm to delete a node in the middle (i.e., any node but
                 the first and last node, not necessarily the exact middle) of a singly
                 linked list, given only access to that node.

    Classes: None

    Functions:

        delete_middle_node Delete node in linked list that is not the head or tail

"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Empty


def delete_middle_node(node):
    """Delete middle node from singly linked list

    \param node node to be deleted

    """
    # Empty node
    if node is None:
        raise Empty("Node is empty")

    # Not a middle node
    elif node.next is None:
        raise IndexError("Not middle node")

    # Copy contents of next node to current node
    tmp = node.next
    node.next = tmp.next
    node.data = tmp.data

    # Delete the next node
    tmp.data = tmp.next = None
