from unittest import TestCase
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Empty, Node
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex6 import PalindromeSinglyLinkedList, is_palindrome_brute_force
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex6 import is_palindrome_reverse


class TestPalindromeSinglyLinkedList(TestCase):

    def setUp(self):
        self.pll = PalindromeSinglyLinkedList()

    def tearDown(self):
        self.pll = None

    def test_empty_list(self):
        with self.assertRaises(Empty):
            self.pll.is_palindrome()

    def test_single_element(self):
        self.pll.add(1)
        self.assertTrue(self.pll.is_palindrome())

    def test_two_elements(self):
        self.pll.add(1)
        self.pll.add(1)

        self.assertTrue(self.pll.is_palindrome())

        self.pll.remove(1)
        self.pll.add(2)

        self.assertFalse(self.pll.is_palindrome())

    def test_more_than_two_elements_even(self):
        self.pll.add(1)
        self.pll.add(2)
        self.pll.add(2)
        self.pll.add(2)

        self.assertFalse(self.pll.is_palindrome())
        self.pll.remove(2)
        self.pll.add(1)

        self.assertTrue(self.pll.is_palindrome())

    def test_more_than_two_elements_odd(self):
        self.pll.add(1)
        self.pll.add(2)
        self.pll.add(2)

        self.assertFalse(self.pll.is_palindrome())
        self.pll.remove(2)
        self.pll.add(1)
        self.assertTrue(self.pll.is_palindrome())


class TestPalindromeBruteForce(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_linked_list(self):
        self.assertIsNone(is_palindrome_brute_force(None))

    def test_single_element(self):
        list = Node(1)
        self.assertTrue(is_palindrome_brute_force(list))

    def test_two_elements(self):
        list = Node(1)
        list.next = Node(2)

        self.assertFalse(is_palindrome_brute_force(list))

        list.next = Node(1)
        self.assertTrue(is_palindrome_brute_force(list))

    def test_odd_elements(self):
        list = Node(1)
        list.next = Node(2)
        list.next.next = Node(2)

        self.assertFalse(is_palindrome_brute_force(list))

        list.next.next = Node(1)

        self.assertTrue(is_palindrome_brute_force(list))

    def test_even_elements(self):
        list = Node(1)
        list.next = Node(2)
        list.next.next = Node(2)
        list.next.next.next = Node(3)

        self.assertFalse(is_palindrome_brute_force(list))

        list.next.next.next = Node(1)

        self.assertTrue(is_palindrome_brute_force(list))


class TestPalindromeReverse(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_node(self):
        self.assertIsNone(is_palindrome_reverse(None))

    def test_single_node(self):
        self.assertTrue(is_palindrome_reverse(Node(1)))

    def test_two_nodes(self):
        l_list = Node(1)
        l_list.next = Node(2)

        self.assertFalse(is_palindrome_reverse(l_list))

        l_list.next = Node(1)
        self.assertTrue(is_palindrome_reverse(l_list))

    def test_odd_nodes(self):
        l_list = Node(1)
        l_list.next = Node(2)
        l_list.next.next = Node(3)

        self.assertFalse(is_palindrome_reverse(l_list))

        l_list.next.next = Node(1)

        self.assertTrue(is_palindrome_reverse(l_list))

    def test_even_nodes(self):
        l_list = Node(1)
        l_list.next = Node(2)
        l_list.next = Node(2)
        l_list.next = Node(3)
        self.assertFalse(is_palindrome_reverse(l_list))

        l_list.next.next = Node(1)

        self.assertTrue(is_palindrome_reverse(l_list))
