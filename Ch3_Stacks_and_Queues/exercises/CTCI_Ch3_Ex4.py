#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch3_Ex4.py
    Author:             Matt Randazzo
    Date created:       12/30/2018
    Date last modified: 12/30/2018
    Python Version:     3.7

    Description: CTCI 3.4 Queue via Stacks
                 Implement a MyQueue class which implements a queue using two stacks.

    Classes:

        MyQueue A queue abstract data type using two stacks as data storage

    Functions:

"""
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full, Stack


class MyQueue:

    def __init__(self):
        self._stack_old = Stack()
        self._stack_new = Stack()

    def __len__(self):
        return len(self._stack_old) + len(self._stack_new)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, e):
        """Add element e to the end of the queue

        :param e Element to be added to the end of the queue

        """
        if self._stack_new.is_full():
            raise Full("Queue is full")
        self._stack_new.push(e)

    def dequeue(self):
        """Remove element off the front of the queue

        :returns Element at the front of the queue

        """
        if self._stack_old.is_empty():
            while not self._stack_new.is_empty():
                self._stack_old.push(self._stack_new.pop())
        e = self._stack_old.pop()

        return e

    def front(self):
        """Return (but do not remove) the front of the queue

        :returns Element at the front of the queue

        """
        if self._stack_old.is_empty():
            while not self._stack_new.is_empty():
                self._stack_old.push(self._stack_new.pop())
        e = self._stack_old.peek()

        return e




