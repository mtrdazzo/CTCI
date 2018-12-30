#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch3_Ex3.py
    Author:             Matt Randazzo
    Date created:       12/29/2018
    Date last modified: 12/29/2018
    Python Version:     3.7

    Description: CTCI 3.3 Stack of Plates
                 Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
                 Therefore, in real life, we would likely start a new stack when the previous stack
                 exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
                 SetOfStacks should be composed of several stacks and should create a new stack once
                 the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
                 behave identically to a single stack (that is pop() should return the same values
                 as it would if there were just a single stack).

                 Also, implement a function popAt(int index)  which performs a pop operation on a
                 specific sub-stack.
    Classes:

        SetOfStacks

    Functions:

"""
from CTCI.Ch3_Stacks_and_Queues.common.common import Empty, Full


class SetOfStacks:

    class _Stack:
        DEFAULT_SIZE = 10

        def __init__(self, size=DEFAULT_SIZE):
            self._data = [None] * size
            self._index = 0

        def __len__(self):
            return self._index

        def __str__(self):
            return str(self._data)

        def is_full(self):
            return self._index == self.DEFAULT_SIZE

        def is_empty(self):
            return self._index == 0

        def push(self, e):
            if self.is_full():
                raise Full("Stack is full")
            self._data[self._index] = e
            self._index += 1

        def pop(self):
            if self.is_empty():
                raise Empty("Stack is empty")
            e = self._data[self._index - 1]
            self._data[self._index - 1] = None
            self._index -= 1

            return e

        def peek(self):
            if self.is_empty():
                raise Empty("Stack is empty")
            return self._data[self._index - 1]

    DEFAULT_SIZE = 10

    def __init__(self):
        """Instantiate class with array of Stacks of length 1"""
        self._stacks = [self._Stack(self.DEFAULT_SIZE)]

    def __len__(self):
        return len(self._stacks)

    def __str__(self):
        s = ""
        for stack in self._stacks:
            s += str(stack) + "\n"
        return s

    def peek(self):
        return self._stacks[-1].peek()

    def push(self, e):
        """Push element e to the first non-full stack

        :param e Element to be pushed to the first non-full stack

        """
        index = 0
        pushed = False

        while index < len(self._stacks) and not pushed:
            if not self._stacks[index].is_full():
                self._stacks[index].push(e)
                pushed = True
            else:
                index += 1

        if not pushed:
            self._stacks.append(self._Stack(self.DEFAULT_SIZE))
            self._stacks[-1].push(e)

    def pop(self):
        """Pop the first element off the first non-empty stack

        :returns Element off the top of the first non-empty stack

        """
        index = 0
        popped = False

        while index < len(self._stacks) and not popped:
            if not self._stacks[index].is_empty():
                e = self._stacks[index].pop()
                popped = True
            else:
                index += 1
        if not popped:
            raise Empty("All stacks are empty")
        return e

    def popAt(self, index):
        """Pop element off the top of the indexed stack

        :param   index Stack index
        :returns Element off the top of the indexed stack

        """
        if index < 1 or index > len(self._stacks):
            raise IndexError(str(index) + " not a valid index")
        e = self._stacks[index - 1].pop()

        # Fill stack, shift following stack contents
        for curr_index in range(index, len(self._stacks)):
            self._stacks[curr_index - 1]._data[-1] = self._fill_stack(self._stacks[curr_index])
            self._shift_stack_left(self._stacks[curr_index])

        # Remove stack if empty
        if self._stacks[len(self._stacks) - 1].is_empty():
            self._stacks.pop()

        return e

    def _fill_stack(self, s):
        """Fill previous stack with next stack's first element

        :param   s Next Stack
        :returns Next stack's first element, None if empty

        """
        if s.is_empty():
            return
        first = s._data[0]
        s._data[0] = None
        s._index -= 1

        return first

    def _shift_stack_left(self, s):
        """Shift elements in a stack to the left

        :param s Stack where elements are to be shifted to the left

        """
        if s.is_empty():
            return
        index = 1

        while index < len(s._data) and s._data[index] is not None:
            s._data[index - 1] = s._data[index]
            index += 1
        s._data[index - 1] = None
        s._index += 1
