#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex2.py
    Author:             Matt Randazzo
    Date created:       12/14/2018
    Date last modified: 12/20/2018
    Python Version:     3.7

    Description: CTCI 2.2 Return Kth to Last
                 Implement an algorithm to find the kth to last element of a singly
                 linked list.
    Classes:

       KthLastSinglyLinkedList SinglyLinkedList with methods added to find kth to last node

    Functions:

        kth_to_last   Iterative solution to return the kth to last node in the linked list
        kth_to_last_r Recursive solution

"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import SinglyLinkedList, Empty


class KthLastSinglyLinkedList(SinglyLinkedList):

    def kth_to_last(self, k):
        """Iterative solution to return the kth to last node in the linked list"""
        #Do nothing
        if self.is_empty():
            raise Empty("List is empty")
        if k < 1:
            raise ValueError("Index must be > 0")

        #Runner technique
        slow = fast = self._head
        while fast._next is not None and k > 1:
            fast = fast._next
            k -= 1

        #Not enough elements
        if k > 1:
            return None

        #Traverse to the end of the linked list
        while fast._next is not None:
            fast = fast._next
            slow = slow._next

        return slow._data

    def kth_to_last_r(self, k):
        """Recursive solution to return the kth to last node """
        self.kth_node = None

        if self.is_empty():
            raise Empty("List is empty")
        elif k < 1:
            raise ValueError("Index must > 0")

        def kth_to_last_helper(node, k):
            if node is None:
                return 1
            n = kth_to_last_helper(node._next, k)

            if k > n:
                return 1 + n
            elif k == n and self.kth_node is None:
                self.kth_node = node._data
            return n

        kth_to_last_helper(self._head, k)

        return self.kth_node
