#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex7.py
    Author:             Matt Randazzo
    Date created:       12/26/2018
    Date last modified: 12/26/2018
    Python Version:     3.7

    Description: CTCI 2.8 Loop Detection
                 Given a circular linked list, implement an alogrithm that returns the node
                 at the beginning of the loop

    Classes:

    Functions:

        loop_detection        Detect loop using two pointers
        loop_detection_buffer Detect loop in a linked list using a buffer, uses O(n) space

"""


def loop_detection(head):
    """Loop detection using two pointer method

    :param   head head of the linked list
    :returns Node at the beginning of the intersection, False if no intersection

    """
    if head is None:
        return False

    fast = slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            break

    if fast is None or fast.next is None:
        return False

    slow = head

    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow

def loop_detection_buffer(head):
    """Brute force method to determine the node at the beginning of the loop

    :param   head head of the linked list
    :returns False or node at the beginning of the loop

    """
    if head is None:
        return False

    curr = head
    nodes = []

    while curr is not None:
        if curr not in nodes:
            nodes.append(curr)
        else:
            return curr
        curr = curr.next

    return False


