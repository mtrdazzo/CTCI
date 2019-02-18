from collections import deque


class BinarySearchTree:
    """Binary Search Tree Class"""
    class Node:
        """Lightweight Tree Node"""
        __slots__ = 'data', 'left', 'right', 'parent'

        def __init__(self, data, parent=None):
            """Tree node constructor

            :param data   node key
            :param parent parent node, (none) if root

            """
            self.data = data
            self.left = None
            self.right = None
            self.parent =parent

        def __str__(self):
            """String representation of node"""
            return str(self.data)

    def __init__(self):
        """Binary Tree Constructor"""
        self.root = None
        self.num = 0

    def __len__(self):
        """Number of elements in the tree"""
        return self.num

    def is_empty(self):
        """Return True if binary tree is empty"""
        return self.num == 0

    def first(self):
        """Find maximum element"""
        return self._find_last_position(self.root) if self.root is not None else None

    def last(self):
        """Find minimum element"""
        return self._find_last_position(self.root) if self.root is not None else None

    def _find_last_position(self, root):
        """Find last position in root

        :param root root of binary tree

        """
        if root is None:
            return
        current = root
        while current.right is not None:
            current = current.right
        return current

    def _find_first_position(self, root):
        """Find first position in root

        :param root root of binary tree

        """
        if root is None:
            return
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, n):
        """Delete node with key value n starting at root"""
        def num_children(node):
            """Return number of children for a node"""
            children = 0
            children += 1 if node.left is not None else 0
            children += 1 if node.right is not None else 0
            return children

        if self.is_empty():
            return

        node = self.search(root, n)

        if node is None:
            return

        node_children = num_children(node)
        node_parent = node.parent

        if node_children == 0: # Leaf node
            if node_parent is None: # Root of binary tree
                self.root = None
            elif node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
            node.left = node.right = node.parent = node.data = None
        elif node_children == 1: # Single child
            if node.left is None:
                tmp = node.right
            else:
                tmp = node.left
            if node_parent.left == node:
                node_parent.left = tmp
            else:
                node_parent.right = tmp
            tmp.parent = node_parent
            node.data = node.left = node.right = node.parent = None
        else:
            # Find next tree successor
            successor = self._find_first_position(node.right).data
            node.data = successor

            # Recursively delete successor
            self.delete(node.right, successor)
        self.num -= 1

    def search(self, root, key):
        """Search for key in Binary Tree

        :param root Binary Tree root
        :param key  Node key

        """
        if root is None or root.data == key:
            return root
        elif root.data < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    def _add_helper(self, root, n):
        """Add node to Binary Tree helper function

        :param root binary tree root
        :param n    node key

        """
        if n > root.data:
            if root.right is None:
                root.right = self.Node(n, root)
                self.num += 1
                return root.right
            else:
                return self._add_helper(root.right, n)
        else:
            if root.left is None:
                root.left = self.Node(n, root)
                self.num += 1
                return root.left
            else:
                return self._add_helper(root.left, n)

    def add(self, n):
        """Add node to binary tree

        :param n node key

        """
        if self.root is None:
            self.root = self.Node(n)
            self.num += 1
            return self.root
        else:
            return self._add_helper(self.root, n)

    def print_right(self):
        """Print right side of the binary tree"""
        if self.is_empty():
            return
        nodes = deque()
        nodes.append(self.root)
        nodes.append(None)
        prev = None

        while len(nodes) > 0:
            p = nodes.popleft()
            if p is None:
                if prev is None:
                    print()
                    return
                else:
                    print(str(prev) + " ", end="")
                    nodes.append(None)
            else:
                nodes.append(p.left) if p.left is not None else None
                nodes.append(p.right) if p.right is not None else None
            prev = p
        print("")

    def print_left(self):
        """Print left side view of binary tree"""
        if self.is_empty():
            return
        nodes = deque()
        nodes.append(self.root)
        nodes.append(None)
        prev = None

        while len(nodes) > 0:
            p = nodes.popleft()
            if p is None:
                if prev is None:
                    print()
                    return
                else:
                    nodes.append(None)
            else:
                if prev is None:
                    print(str(p) + " ", end="")
                nodes.append(p.left) if p.left is not None else None
                nodes.append(p.right) if p.right is not None else None
            prev = p

    def height(self):
        """Return height of Binary Tree

        :return height of binary tree root

        """
        return self.get_height(self.root)

    def get_height(self, node):
        """Return height of node

        :param  node binary tree node
        :return      height of binary tree root

        """
        return self._height_helper(node)

    def _height_helper(self, node):
        if node is None: # Is empty?
            return -1
        else:
            return max(self._height_helper(node.left), self._height_helper(node.right)) + 1

    def print_with_level(self):
        if self.is_empty():
            return
        nodes = deque()
        nodes.append(self.root)
        nodes.append(None)
        prev = None

        while len(nodes) > 0:
            p = nodes.popleft()
            if p is None:
                if prev is None:
                    print()
                    return
                else:
                    print()
                    nodes.append(None)
            else:
                print(str(p) + " ", end="")
                nodes.append(p.left) if p.left is not None else None
                nodes.append(p.right) if p.right is not None else None
            prev = p

    def print_node_structure(self, node):
        if node is None:
            return ""
        q = deque()
        s = []
        q.append(self.root)
        q.append(None)
        s.append(self.root.data)
        s.append(None)
        prev = None

        while len(q) is not None:
            n = q.popleft()
            if n is None:
                if prev is None:
                    print(s)
                    break
                else:
                    s.append(None)
                    q.append(None)
            else:
                if n.left is not None:
                    q.append(n.left)
                    s.append(n.left.data)
                else:
                    s.append(" ")
                if n.right is not None:
                    q.append(n.right)
                    s.append(n.right.data)
                else:
                    s.append(" ")
            prev = n

    def delete_tree1(self):
        """Delete entire binary tree using postorder traversal"""
        if self.is_empty():
            return
        self._delete_tree_helper_postorder(self.root)

    def delete_tree2(self):
        """Non-recursively delete entire binary tree using level order traversal"""
        # Empty tree
        if self.is_empty():
            return
        # Create queue
        queue = deque()
        queue.append(self.root)
        self.root = None

        while len(queue) > 0:
            curr = queue.popleft()

            if curr.left is not None:
                curr.left.parent = None
                queue.append(curr.left)

            if curr.right is not None:
                curr.right.parent = None
                queue.append(curr.right)

            # Memory management (picked up by garbage collector)
            print("Deleting node: " + str(curr))
            curr.data = curr.left = curr.right = curr.parent = None

            self.num -= 1
            print("Number of nodes: " + str(self.num))

    def _delete_tree_helper_preorder(self, root):
        """"Helper function to delete tree using preorder traversal

        :param root binary tree root

        """
        if root is None:
            return
        self.delete(root, root.data)
        self._delete_tree_helper_preorder(root)

    def _delete_tree_helper_postorder(self, root):
        """Helper function to delete tree using postorder traversal

        :param root binary tree root

        """
        # Post order traversal delete
        if root is None:
            return
        self._delete_tree_helper_postorder(root.left)
        self._delete_tree_helper_postorder(root.right)

        print("Deleting node: " + str(root))
        self.delete(root, root.data)

    def __str__(self):
        """Print nodes of binary tree using level order traversal"""
        if self.is_empty():
            return ""

        node_str = ""
        nodes = deque()
        nodes.append(self.root)

        while len(nodes) > 0:
            curr = nodes.popleft()
            node_str += str(curr) + " "
            nodes.append(curr.left) if curr.left is not None else None
            nodes.append(curr.right) if curr.right is not None else None
        return node_str

    def pre_order(self):
        """Pre-order Binary Tree traversal"""
        if self.root is not None:
            print(self.root.key)
            pre_order(self.root.left)
            pre_order(self.root.right)

    def post_order(self):
        """Post-order Binary Tree traversal"""
        if self.root is not None:
            post_order(self.root.left)
            post_order(self.root.right)
            print(self.root.key)

    def in_order(self):
        """In-order Binary Tree traversal"""
        if self.root is not None:
            in_order(self.root.left)
            print(self.root.key)
            in_order(self.root.right)
