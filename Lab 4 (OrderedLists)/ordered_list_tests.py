"""Test File for Lab 4
   Parth Ray
"""

import unittest
from ordered_list import Node
from ordered_list import OrderedList


class TestCase(unittest.TestCase):
    def test_size(self):
        lst = OrderedList()
        self.assertEqual(lst.size(), 0)
        lst.num_items = 20
        self.assertEqual(lst.size(), 20)

    def test_is_empty(self):
        lst = OrderedList()
        self.assertTrue(lst.is_empty())
        lst.num_items = 20
        self.assertFalse(lst.is_empty())

    def test_search_forward(self):
        lst = OrderedList()
        self.assertFalse(lst.search_forward(10))
        lst.head = Node(2, Node(5, Node(10, None)))
        lst.tail = Node(10)
        lst.num_items = 3
        self.assertTrue(lst.search_forward(10))

    def test_search_backward(self):
        lst = OrderedList()
        self.assertFalse(lst.search_backward(10))
        lst.tail = Node(10, None, Node(5, None, Node(3)))
        lst.num_items = 3
        self.assertTrue(lst.search_backward(5))

    def test_add(self):
        lst = OrderedList()
        lst.add(1)
        self.assertEqual(lst.head, Node(1))
        lst.add(3)
        lst.add(2)

    def test_remove(self):
        lst = OrderedList()
        lst.add(1)
        lst.add(3)
        lst.add(2)
        self.assertEqual(lst.remove(1), 0)
        self.assertEqual(lst.remove(3), 1)
        self.assertRaises(ValueError, lst.remove, 3)

    def test_index(self):
        lst = OrderedList()
        self.assertRaises(LookupError, lst.index, 5)
        lst.head = Node(2, Node(5, Node(10, None)))
        lst.num_items = 3
        self.assertEqual(lst.index(5), 1)
        self.assertEqual(lst.index(2), 0)
        self.assertEqual(lst.index(10), 2)

    def test_pop(self):
        lst = OrderedList()
        self.assertRaises(IndexError, lst.pop)
        lst.add(1)
        lst.add(3)
        lst.add(2)
        self.assertRaises(IndexError, lst.pop, 3)
        self.assertEqual(lst.pop(1), 2)
        self.assertEqual(lst.pop(0), 1)
        lst.add(4)
        self.assertEqual(lst.pop(), 4)
        self.assertEqual(lst.pop(), 3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
