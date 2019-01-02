#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch3_Ex6.py
    Author:             Matt Randazzo
    Date created:       12/31/2018
    Date last modified: 1/1/2019
    Python Version:     3.7

    Description: CTCI 3.6 Animal Shelter
                 An animal shelter, which holds only dogs and cats, operates on a strictly
                 "first in, first out" basis. People must adopt either the "oldest" (based
                 on arrival time) of all animals at the shelter, or they can select
                 whether they would prefer a dog or a cat (and will receive the oldest
                 animal of that type). They cannot select which specific animal they would
                 like. Create the data structures to maintain this system and implement
                 operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may
                 use the built-in LinkedList data structure.

    Classes:

        AnimalShelter

    Functions:

"""
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import LinkedList, Empty


class Animal:
    __slots__ = '_name'

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __str__(self):
        return str(("Dog", self.name))


class Cat(Animal):
    def __str__(self):
        return str(("Cat", self.name))


class AnimalShelter:

    def __init__(self):
        self._list = LinkedList()

    def __str__(self):
        if self._list.head is None:
            return ""
        return str(self._list.head)

    def enqueue(self, a):
        """Add animal a to the end of the list"""
        if not isinstance(a, (Dog, Cat)):
            raise TypeError("Not a valid input")
        self._list.add(a)

    def dequeueAny(self):
        """Dequeue oldest element in the linked list

        :returns Oldest animal in the list

        """
        if self._list.head is None:
            raise Empty("List is empty")

        e = self._list.head.data
        self._list.head = self._list.head.next

        return e

    def dequeueDog(self):
        """Dequeue oldest dog in the linked list

        :returns Oldest dog in the list

        """
        if self._list.head is None:
            raise Empty("List is empty")

        curr = self._list.head

        if isinstance(curr.data, Dog):
            e = self._list.head.data
            self._list.head = self._list.head.next
            return e

        while curr.next is not None:
            if isinstance(curr.next.data, Dog):
                e = curr.next.data
                curr.next = curr.next.next
                return e
            curr = curr.next
        raise Empty("No dogs in queue")

    def dequeueCat(self):
        """Dequeues oldest cat in the linked list

        :returns Oldest cat in the list

        """
        if self._list.head is None:
            raise Empty("List is empty")

        curr = self._list.head

        if isinstance(curr.data, Cat):
            e = self._list.head.data
            self._list.head = self._list.head.next
            return e

        while curr.next is not None:
            if isinstance(curr.next.data, Cat):
                e = curr.next.data
                curr.next = curr.next.next
                return e
            curr = curr.next
        raise Empty("No cats in queue")
