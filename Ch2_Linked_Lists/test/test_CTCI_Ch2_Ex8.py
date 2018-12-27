from unittest import TestCase
from CTCI.Ch2_Linked_Lists.exercises.CTCI_Ch2_Ex8 import loop_detection_buffer, loop_detection
from CTCI.Ch2_Linked_Lists.common.SinglyLinkedList import Node


class TestLoopDetection(TestCase):

    def setUp(self):
        self.ll = Node(0)

    def tearDown(self):
        pass

    def test_empty_list(self):
        self.assertFalse(loop_detection(None))

    def test_single_element(self):

        # No loop
        self.assertFalse(loop_detection(self.ll))

        # Has loop
        self.ll.next = self.ll
        self.assertTrue(loop_detection(self.ll))

    def test_multiple_elements(self):
        self.ll.next = Node(1)

        # No loop
        self.assertFalse(loop_detection(self.ll))

        # Loop at end
        self.ll.next.next = self.ll.next
        self.assertTrue(loop_detection(self.ll) == self.ll.next)

        # Loop at beginning
        self.ll.next.next = Node(2)
        self.ll.next.next.next = self.ll.next

        self.assertTrue(loop_detection(self.ll) == self.ll.next)


class TestLoopDetectionBuffer(TestCase):
    def setUp(self):
        self.ll = Node(0)

    def tearDown(self):
        pass

    def test_empty_list(self):
        self.assertFalse(loop_detection_buffer(None))

    def test_no_loop(self):
        self.assertFalse(loop_detection_buffer(self.ll))

        self.ll.next = Node(1)
        self.ll.next.next = Node(3)

        self.assertFalse(loop_detection_buffer(self.ll))

    def test_loop(self):
        self.ll.next = self.ll

        # Single element
        self.assertTrue(loop_detection_buffer(self.ll) == self.ll)

        # Loop at beginning
        self.ll.next = Node(1)
        self.ll.next.next = self.ll
        self.assertTrue(loop_detection_buffer(self.ll) == self.ll)

        # Loop in middle
        self.ll.next.next = Node(2)
        self.ll.next.next = self.ll.next
        self.assertTrue(loop_detection_buffer(self.ll) == self.ll.next)

        # Loop at end
        self.ll.next.next.next = self.ll.next.next
        self.assertTrue(loop_detection_buffer(self.ll) == self.ll.next.next)

