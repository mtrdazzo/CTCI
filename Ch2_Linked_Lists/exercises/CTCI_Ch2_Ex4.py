#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex4.py
    Author:             Matt Randazzo
    Date created:       12/20/2018
    Date last modified: 12/20/2018
    Python Version:     3.7

    Description: CTCI 2.4 Partition
                 Write code to partition  a linked list around a value x, such that all
                 nodes less than x come before all nodes greater than or equal to x. If
                 x is contained within the list, the values of x only need to be after
                 the elements less than x (see below). The partition element x can appear
                 anywhere in teh "right partition"; it does not need to appear between
                 the left and right partitions.
    Classes:

       PartitionSinglyLinkedList SinglyLinkedList class with partition method

    Functions:

        partition Partition linked list based on a value

"""

from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import SinglyLinkedList,Empty

class PartitionSinglyLinkedList(SinglyLinkedList):

    def partition(self, value):
        """Partition linked list separated by node with value

        Solution: Separate values into two singly linked list, one with elements less than
                  value and the other with elements greater than or equal to value. Then
                  join linked lists together.

        \param value Pivot node value

        """

        # Empty condition
        if self.is_empty():
            raise Empty("List is empty")

        # Verify pivot value exists, or else return None
        pivot = self._head
        while pivot is not None:
            if pivot._data == value:
                break
            pivot = pivot._next

        if pivot is None:
            return

        # Create pointers to two linked lists
        ptr1 = ptr2 = None
        curr = self._head
        self._head = None

        while curr is not None:
            tmp = curr
            curr = curr._next
            tmp._next = None

            # Left partition
            if tmp._data < value:
                if ptr1 is None:
                    ptr1 = ptr1_curr = tmp
                else:
                    ptr1_curr._next = tmp
                    ptr1_curr = ptr1_curr._next
            # Right partition
            else:
                if ptr2 is None:
                    ptr2 = ptr2_curr = tmp
                else:
                    ptr2_curr._next = tmp
                    ptr2_curr = ptr2_curr._next

        # Join linked lists together
        if ptr1 is not None:
            self._head = ptr1
            ptr1_curr._next = ptr2
        else:
            self._head = ptr2
        if ptr2 is not None:
            self._tail = ptr2_curr
        else:
            self._tail = ptr1_curr
