#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex7.py
    Author:             Matt Randazzo
    Date created:       12/24/2018
    Date last modified: 12/24/2018
    Python Version:     3.7

    Description: CTCI 2.7 Intersection
                 Given two (singly) linked lists, determine if the two lists intersect.
                 Return the intersecting node. Note that the intersection is defined based
                 on reference, not value. That is, if the kth node of the first linked list
                 is the exact same node (by reference) as the jth node of the second linked
                 list, then they are intersecting.
    Classes:


    Functions:

"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Node


def is_intersection(ll_a, ll_b):
    """Determine if intersection occurs between linked lists

    :param   ll_a head of linked list a
    :param   ll_b head of linked list b
    :returns False if no intersection or node of intersection

    """
    if ll_a is None or ll_b is None:
        return False

    curr_a = ll_a
    curr_b = ll_b

    while curr_a.next is not None:
        curr_a = curr_a.next

    while curr_b.next is not None:
        curr_b = curr_b.next

    if curr_a is not curr_b:
        return False

    size_a = 0
    size_b = 0

    curr_a = ll_a
    curr_b = ll_b

    # Find lengths of linked lists
    while curr_a is not None:
        curr_a = curr_a.next
        size_a += 1

    while curr_b is not None:
        curr_b = curr_b.next
        size_b += 1

    if size_a < size_b:
        shorter = ll_a
        longer = ll_b
    elif size_b <= size_a:
        shorter = ll_b
        longer = ll_a

    diff = abs(size_a - size_b)

    # Pad zeros
    if diff > 0:
        head = new = Node(0)

        while diff - 1:
            new.next = Node(0)
            new = new.next
            diff = diff - 1

        new.next = shorter
        shorter = head

    # Increment through both lists, find intersection
    while shorter is not None:
        if shorter is longer:
            return shorter
        shorter = shorter.next
        longer = longer.next

    return False
