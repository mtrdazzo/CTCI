#!/usr/bin/env python
"""
    File name:          CTCI_Ch3_Ex2.py
    Author:             Matt Randazzo
    Date created:       12/27/2018
    Date last modified: 12/27/2018
    Python Version:     3.7

    Description: CTCI 3.2 Stack Min
                 How would you design a stack which, in addition to push and pop, has a function
                 min which returns the minimum element? Push, pop, and min should all operate in
                 O(1) time.
    Classes:

        MinStack Data Structure that has the function min to return the minimum element in O(1)
                 time

    Functions:

"""
from CTCI.Ch3_Stacks_and_Queues.common.common import Stack, Empty, Full


class MinStack(Stack):
    """LIFO implementation of a Stack using a list as data storage"""
    DEFAULT_SIZE = 20

    def __init__(self):
        """Instantiate an empty stack"""
        self._data = [None] * self.DEFAULT_SIZE
        self._size = 0
        self._min = [None] * self.DEFAULT_SIZE

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def __str__(self):
        """Print the data in the stack"""
        return str(self._data)

    def is_empty(self):
        """Return True if there are no elements in the stack"""
        return self._size == 0

    def push(self, e):
        """Push an element e to the top of the stack

        :param e Element to be pushed on the top of the stack

        """
        if self._size == self.DEFAULT_SIZE:
            raise Full("Stack is full!")
        self._data[self._size] = e

        if self.is_empty():
            self._min[self._size] = e
        else:
            self._min[self._size] = min(e, self._min[self._size - 1])

        self._size += 1

    def min(self):
        """Returns the minimum element in the stack O(n) space, O(1) time

        :returns Minimum element in the stack

        """
        if self.is_empty():
            return
        return self._min[self._size - 1]

    def pop(self):
        """Pop the element off the top of the stack

        :returns Element on the top of the stack

        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        e = self._data[self._size-1]

        self._data[self._size-1] = None
        self._min[self._size-1] = None
        self._size -= 1
        self._min.pop()

        return e

    def peek(self):
        """Return but do not remove the element off the top of the stack

        :returns Element on the top of the stack

        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[self._size - 1]
