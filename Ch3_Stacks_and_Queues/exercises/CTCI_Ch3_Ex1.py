#!/usr/bin/env python
"""
    File name:          CTCI_Ch3_Ex1.py
    Author:             Matt Randazzo
    Date created:       12/27/2018
    Date last modified: 12/27/2018
    Python Version:     3.7

    Description: CTCI 3.1 Three In One
                 Describe how you could use a single array to implement three stacks.

    Classes:

        ThreeInOneStack Data Structure that uses a list to hold three stacks with fixed size

    Functions:

"""
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full


class ThreeInOneStack:
    """Create a list to hold three stacks of equal fixed size"""

    NUMBER_OF_STACKS = 3
    STACK_SIZE = 10

    class Stack:
        """Stack Class"""
        def __init__(self):
            """Create an empty stack"""
            self.index = 0

        def is_full(self):
            """Return True if index has been incremented to stack's maximum size"""
            return self.index == ThreeInOneStack.STACK_SIZE

        def is_empty(self):
            """Return True if index has not been incremented from 0"""
            return self.index == 0

    def __init__(self):
        """Create a data structure with STACK_SIZE * NUMBER_OF_STACKS data references
           and NUMBER_OF_STACKS references."""
        self.data = [None] * self.STACK_SIZE * self.NUMBER_OF_STACKS
        self.stacks = [self.Stack() for _ in range(self.NUMBER_OF_STACKS)]

    def __str__(self):
        """Print the array of data references"""
        return str(self.data)

    def _get_stack_index_reference(self, s):
        """Get the most recent index from the stack s

        :param   s Stack number (1-3)
        :returns Most recent index on the stack s

        """
        if self.stacks[s - 1].is_empty():
            s_index = 0
        else:
            s_index = self.stacks[s - 1].index

        return self.STACK_SIZE * (s - 1) + s_index

    def push(self, e, s):
        """Push an element e onto stack s

        :param e Element to be pushed
        :param s Stack number (1-3)

        """
        if e is None:
            return

        if s not in range(1, 4):
            raise IOError(str(s) + " not in valid stack range (1-3)")

        if self.stacks[s - 1].is_full():
            raise Full("Stack is full!")

        index = self._get_stack_index_reference(s)
        self.stacks[s - 1].index += 1

        self.data[index] = e

    def pop(self, s):
        """Pop the element off the top of the stack s

        :param   s Stack number (1-3)
        :returns The reference to the element at the top of the stack s

        """
        if s not in range(1, 4):
            raise IOError(str(s) + " not in valid stack range (1-3)")

        if self.stacks[s - 1].is_empty():
            raise Empty("Stack is empty!")

        index = self._get_stack_index_reference(s) - 1

        e = self.data[index]

        self.data[index] = None
        self.stacks[s - 1].index -= 1

        return e

    def peek(self, s):
        """Return but do not pop the top element off the top of the stack s

        :param   s Stack number (1-3)
        :returns Reference to the element on the top of the stack s

        """
        if s not in range(1, 4):
            raise IOError(str(s) + " not in valid stack range (1-3)")

        if self.stacks[s - 1].is_empty():
            raise Empty("Stack is empty!")

        index = self._get_stack_index_reference(s) - 1

        return self.data[index]

