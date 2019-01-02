#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch3_Ex5.py
    Author:             Matt Randazzo
    Date created:       12/30/2018
    Date last modified: 12/30/2018
    Python Version:     3.7

    Description: CTCI 3.5 Sort Stack
                 Write a program to sort a stack such that the smallest items are on the
                 top. You can use an additional temporary stack, but you may not copy the elements
                 into any other data structure (such as an array). The stack supports the
                 following operations: push, pop, peek, and isEmpty.

    Classes:

    Functions:

        sort_stack Sort elements with smallest elements on top of the stack

"""
from CTCI.Ch3_Stacks_and_Queues.common.common import Stack


def sort_stack(input_stack):
    tmp_stack = Stack()

    while not input_stack.is_empty():
        new = input_stack.pop()
        if tmp_stack.is_empty() or new > tmp_stack.peek():
            tmp_stack.push(new)
        else:
            while not tmp_stack.is_empty() and tmp_stack.peek() > new:
                input_stack.push(tmp_stack.pop())
            tmp_stack.push(new)

    while not tmp_stack.is_empty():
        input_stack.push(tmp_stack.pop())

    return input_stack
