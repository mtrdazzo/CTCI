#!/usr/bin/env python
"""
    File name:          CTCI_Ch2_Ex6.py
    Author:             Matt Randazzo
    Date created:       12/24/2018
    Date last modified: 12/24/2018
    Python Version:     3.7

    Description: CTCI 2.6 Palindrome

                 Implement a function to check if a linked list is a palindrome.

    Classes:

        PalindromeSinglyLinkedList Singly linked list with is_palindrome function

    Functions:

        is_palindrome Return True if linked list is a palindrome

"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import SinglyLinkedList, Empty
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import LinkedStack


class PalindromeSinglyLinkedList(SinglyLinkedList):

    def is_palindrome(self):
        """Determine if linked list is a palindrome

        :returns Boolean if linked list is a palindrome

        """

        if self.is_empty():
            raise Empty("List is empty")
        elif len(self) == 1:
            return True

        def is_palindrome_helper(node_end):
            """Helper function to check if list is a palindrome

            :param   node_end   node at end of the list

            :returns True if linked list is a palindrome"""

            if node_end is None:
                return self._head

            node_begin = is_palindrome_helper(node_end._next)

            if node_begin is True:
                return True
            elif node_begin is False:
                return False
            elif node_begin._data != node_end._data:
                return False
            else:
                if node_begin is node_end:
                    return True
                if node_begin._next is node_end:
                    return True
                else:
                    return node_begin._next

        return is_palindrome_helper(self._head)


def is_palindrome_brute_force(head):
    """Brute force method to test if linked list is a palindrome

    :param   head Head of the linked list
    :returns Boolean if linked list is a palindrome

    """
    if head is None:
        return

    curr = head
    stack = LinkedStack()

    while curr is not None:
        stack.push(curr.data)
        curr = curr.next

    curr = head

    while curr is not None:
        if curr.data != stack.pop():
            return False
        curr = curr.next
    return True


def is_palindrome_reverse(head):
    """Return if linked list is a palindrome by reversing the second half of the linked list

    :param   head Head of the linked list

    :returns Boolean if linked list is a palindrome

    """
    if head is None:
        return

    if head.next is None:
        return True

    def reverse_linked_list(head):
        """Iteratively reverse the linked list

        :param head of the linked list

        """
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    def find_middle_node(head):
        """Return middle node of the linked list

        :param   head head of the linked list

        :returns Returns the middle, node whether the linked list has an odd or even number of nodes

        """
        fast = slow = head
        num = 0

        while fast.next is not None:
            fast = fast.next
            num += 1
            if fast.next is not None:
                fast = fast.next
                num += 1
            slow = slow.next

        if num % 2:
            is_odd = False
        else:
            is_odd = True

        return slow, is_odd

    head_end, is_odd = find_middle_node(head)

    curr_end = head_end
    if is_odd:
        curr_end = curr_end.next

    # Reverse second half of the linked list
    reverse_linked_list(curr_end)

    curr_begin = head

    cond = True
    while curr_begin is not head_end:
        if curr_begin.data != curr_end.data:
            cond = False
            break
        curr_begin = curr_begin.next
        curr_end = curr_end.next

    reverse_linked_list(head_end)

    return cond
