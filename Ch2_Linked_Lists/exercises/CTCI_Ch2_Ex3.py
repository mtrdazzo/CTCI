#!/usr/bin/env python
"""
    File name: CTCI_Ch2_Ex3.py
    Author: Matt Randazzo
    Date created: 12/14/2018
    Date last modified: 12/14/2018
    Python Version: 3.7

    Description: CTCI 2.2 Return Kth to Last
                 Implement an algorithm to find the kth to last element of a singly
                 linked list.
    Classes:
        Empty               Singly linked list empty exception
        Singly Linked List  Singly linked list ADT

    Functions:
        find_kth_node   Iterative solution to find the kth node of the sinly linked list
        find_kth_node_r Recursive solution to finding the kth node of the singly linked list

"""

class Empty(Exception):
    """Empty Singly Linked List Exception"""
    pass

class SinglyLinkedList:
    """Singly linked list"""

    class _Node:
        """Lightweight non-public node structure"""
        __slots__ = 'data', 'next'
        def __init__(self, data):
            """Create a new node with reference to data"""
            self.data = data
            self.next = None

    def __init__(self):
        """Create an empty singly linked list"""
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """Return the number of element in the linked list"""
        return self.size

    def __str__(self):
        """Print the linked list EX. 1->2->3"""
        if self.is_empty():
            return ""
        curr = self.head
        s = str(curr.data)
        while curr.next is not None:
            curr = curr.next
            s += "->" + str(curr.data)
        return s

    def is_empty(self):
        """Return True if the linked list contains no elements"""
        return len(self) == 0

    def add(self, e):
        """Add a node to the end of the linked list"""
        new = self._Node(e)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def kth_to_last(self, k):
        """Iterative solution to return the kth to last node in the linked list"""
        #Do nothing
        if self.is_empty():
            raise Empty("List is empty")
        if k < 1:
            raise ValueError("Index must be > 0")

        #Runner technique
        slow = fast = self.head
        while fast.next is not None and k > 1:
            fast = fast.next
            k -= 1

        #Not enough elements
        if k > 1:
            return None

        #Traverse to the end of the linked list
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        return slow.data

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
            n = kth_to_last_helper(node.next, k)

            if k > n:
                return 1 + n
            elif k == n and self.kth_node is None:
                self.kth_node = node.data
            return n

        kth_to_last_helper(self.head, k)

        return self.kth_node


