#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex5.py
    Author:             Matt Randazzo
    Date created:       12/21/2018
    Date last modified: 12/21/2018
    Python Version:     3.7

    Description: CTCI 2.5 Sum Lists
                 You have two numbers represented by a linked list, where each node
                 contains a single digit. The digits are stored in reverse order,
                 such that the 1's digit is at the head of the list. Write a function
                 that adds the two numbers and returns the sum as a linked list.
    Classes:


    Functions:

        sum_linked_lists


"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Node, SinglyLinkedList


def sum_linked_lists(node1, node2, carry=0):
    """Recursive solution two linked lists without explicit Singly
       Linked List Class
    
    :param node1 node of first linked list
    :param node2 node of second linked list
    :param carry should be defaulted to zero

    :return Sum of linked lists

    """
    if node1 is None and node2 is None and carry == 0:
        return

    data = carry

    if node1 is not None:
        data += node1.data
        node1 = node1.next

    if node2 is not None:
        data += node2.data
        node2 = node2.next

    curr = Node(data % 10)

    curr.next = sum_linked_lists(node1, node2, int(data >= 10))

    return curr


