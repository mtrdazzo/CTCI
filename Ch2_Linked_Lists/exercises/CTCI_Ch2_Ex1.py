#!/usr/bin/env python
"""
    File name: CTCI_Ch2_Ex1.py
    Author: Matt Randazzo
    Date created: 12/15/2018
    Date last modified: 12/20/2018
    Python Version: 3.7

    Description: CTCI 2.1 Remove Dups
                 Write code to remove duplicates from an unsorted linked list.
    Classes:

        RemoveDupsSinglyLinkedList SinglyLinkedList with method to removes duplicates

    Functions:

        remove_dups_iterative Iterative solution to remove duplicates from linked list
"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import SinglyLinkedList, Empty


class RemoveDupsSinglyLinkedList(SinglyLinkedList):
    """Singly Linked List class with methods to remove duplicates"""

    def remove_dups_iterative(self):
        """Iteratively remove duplicates from the linked list"""
        if self.is_empty():
            raise Empty("List is empty")

        curr = self._head

        while curr is not None:
            ptr1 = curr
            ptr2 = ptr1._next
            while ptr2 is not None:
                if ptr2._data == curr._data:
                    ptr1._next = ptr2._next

                    is_tail = False
                    if ptr2 is self._tail:
                        is_tail = True
                    ptr2 = ptr1

                    if is_tail:
                        self._tail = ptr2

                    self._size -= 1
                else:
                    ptr1 = ptr1._next
                ptr2 = ptr2._next

            curr = curr._next



