class Empty(Exception):
    """Stack or Queue is empty"""
    pass


class Full(Exception):
    """Stack or Queue is full"""
    pass


class Stack:
    """LIFO implementation of a Stack using a list as data storage"""
    DEFAULT_SIZE = 20

    def __init__(self):
        """Instantiate an empty stack"""
        self._data = [None] * self.DEFAULT_SIZE
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def __str__(self):
        """Print the data in the stack"""
        return str(self._data)

    def is_empty(self):
        """Return True if there are no elements in the stack"""
        return self._size == 0

    def is_full(self):
        """Return True if the stack is full"""
        return len(self) == len(self._data)

    def push(self, e):
        """Push an element e to the top of the stack

        :param e Element to be pushed on the top of the stack

        """
        if self._size == self.DEFAULT_SIZE:
            raise Full("Stack is full!")
        self._data[self._size] = e

        self._size += 1

    def min(self):
        """Returns the minimum element in the stack O(n) space, O(1) time

        :returns Minimum element in the stack

        """
        if self.is_empty():
            return

    def pop(self):
        """Pop the element off the top of the stack

        :returns Element on the top of the stack

        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        e = self._data[self._size-1]

        self._data[self._size-1] = None
        self._size -= 1

        return e

    def peek(self):
        """Return but do not remove the element off the top of the stack

        :returns Element on the top of the stack

        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[self._size - 1]
