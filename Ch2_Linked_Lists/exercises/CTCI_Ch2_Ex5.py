#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex5.py
    Author:             Matt Randazzo
    Date created:       12/21/2018
    Date last modified: 12/21/2018
    Python Version:     3.7

    Description: CTCI 2.5 Sum Lists
                 You have two numbers represented by a linked list, where each node
                 contains a single digit. The digits are stored in reverse order,
                 such that the 1's digit is at the head of the list. Write a function
                 that adds the two numbers and returns the sum as a linked list.
    Classes:

        SumSinglyLinkedList SinglyLinkedList class with sum_linked_lists method

    Functions:

        sum_linked_lists        Recursively sum linked list
        sum_linked_list_reverse Sum linked list in reverse order


"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Node, SinglyLinkedList

class SumSinglyLinkedList(SinglyLinkedList):

    def sum_linked_lists(self, other):
        """Recursive solution to summing two linked lists using SinglyLinkedList class
        
        :param   other Other linked list
        :returns sum of two linked lists

        """
        if self.is_empty() and other.is_empty():
            return

        new = SumSinglyLinkedList()

        def sum_helper(node1, node2, carry=0):
            """Sum helper function

            :param   head of linked list
            :param   head of other linked list
            :param   defaulted to zero

            :returns None"""
            if node1 is None and node2 is None and carry == 0:
                return

            data = carry

            if node1 is not None:
                data += node1._data
                node1 = node1._next

            if node2 is not None:
                data += node2._data
                node2 = node2._next

            new.add(data % 10)

            sum_helper(node1, node2, int(data >= 10))

        sum_helper(self._head, other._head)

        return new


def sum_linked_lists(node1, node2, carry=0):
    """Recursive solution summing two linked lists without explicit Singly
       Linked List Class
    
    :param   node1 node of first linked list
    :param   node2 node of second linked list
    :param   carry should be defaulted to zero

    :returns Sum of linked lists

    """
    if node1 is None and node2 is None and carry == 0:
        return

    data = carry

    if node1 is not None:
        data += node1.data
        node1 = node1.next

    if node2 is not None:
        data += node2.data
        node2 = node2.next

    curr = Node(data % 10)

    curr.next = sum_linked_lists(node1, node2, int(data >= 10))

    return curr


def sum_linked_list_reverse(node1, node2, carry=0):

    def pad_zeroes(head, num):
        """Pad zeroes to the front of the linked list

        :param   head head of the linked list
        :param   num  number of zeroes to add
        :returns linked list with zeroes padded to the front

        """
        new = curr = Node(0)
        num -= 1

        while num > 0:
            curr.next = Node(0)
            curr = curr.next
            num -= 1
        curr.next = head
        return new

    def get_length(head):
        """Find length of linked list

        :param   head head of the linked list
        :returns number of elements in the linked list

        """
        num = 0
        curr = head
        while curr is not None:
            curr = curr.next
            num += 1
        return num

    def sum_helper(node1, node2):
        """Sum helper function to recursively sum elements of equal length linked lists

        :param   node1 head of first linked list
        :param   node2 head of second linked list

        :returns sum of first and second linked lists as a set of nodes

        """
        if node1 is None and node2 is None:
            return
        curr = sum_helper(node1.next, node2.next)

        if curr is None:
            curr = Node(0)
        data = node1.data + node2.data + curr.data
        curr.data = data % 10

        next = Node(int(data >= 10))
        next.next = curr

        return next

    len1 = get_length(node1)
    len2 = get_length(node2)

    if len1 < len2:
        node1 = pad_zeroes(node1, len2 - len1)
    elif len2 < len1:
        node2 = pad_zeroes(node2, len1 - len2)

    tmp = sum_helper(node1, node2)

    if tmp.data == 0 and tmp.next is not None:
        tmp = tmp.next

    return tmp
