class Empty(Exception):
    """Empty Linked list exception"""
    pass

class Node:
    """Lightweight, public node class"""
    __slots__ = 'data', 'next'

    def __init__(self, data):
        """Node constructor"""
        self.data = data
        self.next = None

    def __str__(self):
        """Print Linked List"""
        if self.data is None:
            return ""
        curr = self
        retstr = str(curr.data)
        while curr.next is not None:
            curr = curr.next
            retstr += "->" + str(curr.data)
        return retstr


class SinglyLinkedList:
    """Singly Linked List ADT"""

    class _Node:
        """Lightweight, non-public node class"""
        __slots__ = '_data', '_next'

        def __init__(self, data):
            """Node constructor"""
            self._data = data
            self._next = None

    def __init__(self):
        """Create an empty singly linked list"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linked list"""
        return self._size

    def __str__(self):
        """Print the linked list e.g. 1->3->4"""
        if self.is_empty():
            return ""
        curr = self._head
        pstr = str(curr._data)

        while curr._next is not None:
            curr = curr._next
            pstr += "->" + str(curr._data)
        return pstr

    def head(self):
        """Return the head of the linked list"""
        return self._head._data

    def tail(self):
        """Return the tail of the linked list"""
        return self._tail._data

    def is_empty(self):
        """Return True if the number of elements in the linked list is zero"""
        return self._size == 0

    def add(self, e):
        """Add element e to the end of the linked list"""
        new = self._Node(e)
        if not self.is_empty():
            self._tail._next = new
        else:
            self._head = new
        self._tail = new
        self._size += 1

    def remove(self, e):
        """Remove node from the linked list"""

        #Check Empty case
        if self.is_empty():
            raise Empty("Linked list is empty")
        prev = None
        curr = self._head

        #Check if node is head
        if curr._data == e:
            self._head = self._head._next
            tmp = curr._data
            curr._data = curr._next = None
            return tmp
        else:
            found = False
            prev = curr
            curr = curr._next

            while curr is not None and not found:
                if curr._data == e:
                    found = True
                    prev._next = curr._next

                    #Tail condition
                    if curr is self._tail:
                        self._tail = prev
                    tmp = curr._data
                    curr._data = curr._next = None
                    return tmp
                else:
                    prev = curr
                    curr = curr._next

