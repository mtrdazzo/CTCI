#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch4_Ex2.py
    Author:             Matt Randazzo
    Date created:       2/16/2019
    Date last modified: 2/17/2019
    Python Version:     3.7

    Description: CTCI 4.6  Successor
                 Write an algorithm to find the "next" node (i.e., in-order successor) of a given
                 node in a binary search tree. You may assume that each node has a linke to its
                 parent.
    Classes:

            None

    Functions:

            find_successor

"""
from collections import deque


class TreeParent:

    class Node:
        def __init__(self, data, parent=None):
            self.data = data
            self.left = None
            self.right = None
            self.parent = parent

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None
        self._n = 0

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def find(self, k, node=None):
        if self.is_empty():
            return
        if node is None:
            node = self.root
        return self._find_helper(k, node)

    def _find_helper(self, k, root):
        if root is None or root.data == k:
            return root
        elif root.data > k:
            return self._find_helper(k, root.left)
        elif root.data < k:
            return self._find_helper(k, root.right)

    def add(self, key, node=None):
        if self.root is None:
            self.root = self.Node(key)
            self._n += 1
            return self.root
        else:
            if node is None:
                return self._add_helper(key, self.root)
            else:
                return self._add_helper(key, node)

    def _add_helper(self, key, root):
        if root is None:
            return
        if key <= root.data:
            if root.left is None:
                root.left = self.Node(key, root)
                self._n += 1
                return root.left
            else:
                return self._add_helper(key, root.left)
        else:
            if root.right is None:
                root.right = self.Node(key, root)
                self._n += 1
                return root.right
            else:
                return self._add_helper(key, root.right)

    def print_with_level(self):
        if self.is_empty():
            return ""

        q = deque()
        q.append(self.root)
        q.append(None)
        prev = None

        while len(q) > 0:
            n = q.popleft()
            if n is None:
                print()
                if prev is None:
                    return
                else:
                    q.append(None)
            else:
                print(str(n) + " ", end="" )
                q.append(n.left) if n.left is not None else None
                q.append(n.right) if n.right is not None else None

            prev = n

    def find_successor(self, k):
        """Find successor of node with key k

        :param k node key
        :return  successor node

        """
        search = self.find(k)

        if search is None:
            return
        elif search.right is not None:
            walk = search.right
            while walk.left is not None:
                walk = walk.left
            return walk
        else:
            parent = search.parent
            walk = search
            while parent is not None and parent.right == walk:
                walk = parent
                parent = parent.parent
            return parent


if __name__ == '__main__':
    T = TreeParent()

    nodes = [5, 3, 10, 6, 7, 2, 4]
    for node in nodes:
        T.add(node)

    T.print_with_level()
    print(T.find_successor(4))
