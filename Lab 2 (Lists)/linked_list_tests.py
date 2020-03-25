import unittest
from linked_list import Node
from linked_list import insert
from linked_list import get
from linked_list import search
from linked_list import contains
from linked_list import remove
from linked_list import pop
from linked_list import size

class TestCase(unittest.TestCase):
    def test_insert(self):
        self.assertEqual(insert(Node(1, Node(2, None)), 3, 1), Node(1, Node(3, Node(2, None))))
        self.assertEqual(insert(Node(1, Node(2, None)), 50, 0), Node(50, Node(1, Node(2, None))))
        self.assertRaises(IndexError, insert, None, 2, 7)
        self.assertEqual(insert(Node(2, None), 2, 1), Node(2, Node(2, None)))


    def test_get(self):
        self.assertEqual(get(Node(1, Node(2, None)), 1), 2)
        self.assertEqual(get(Node(20, Node(12, None)), 0), 20)
        self.assertRaises(IndexError, get, Node(1, Node(2, None)), 7)


    def test_search(self):
        self.assertEqual(search(Node(1, Node(2, None)), 1), 0)
        self.assertEqual(search(Node(1, Node(2, None)), 70), None)
        self.assertEqual(search(Node(20, Node(50, None)), 50), 1)


    def test_contains(self):
        self.assertTrue(contains(Node(1, Node(2, None)), 1))
        self.assertFalse(contains(Node(1, Node(92, None)), 70))
        self.assertTrue(contains(Node(20, Node(50, None)), 50))


    def test_remove(self):
        self.assertEqual(remove(Node(1, Node(2, None)), 10), Node(1, (Node(2, None))))
        self.assertEqual(remove(None, 20), None)
        self.assertEqual(remove(Node(1, Node(2, Node(3, None))), 2), Node(1, Node(3, None)))


    def test_pop(self):
        self.assertEqual(pop(Node(1, Node(2, Node(3, None))), 2), (Node(1, Node(2, None)), 3))
        self.assertRaises(IndexError, pop, None, 7)
        self.assertEqual(pop(Node(1, Node(2, Node(3, None))), 0), (Node(2, Node(3, None)), 1))


    def test_size(self):
        self.assertEqual(size(Node(1, Node(2, None))), 2)
        self.assertEqual(size(None), 0)
        self.assertEqual(size(Node(1, Node(2, Node(3, None)))), 3)


    def test_str(self):
        self.assertEqual(str(Node(3, None)), "Node(3, None)")
        self.assertEqual(str(None), "None")
        self.assertEqual(str(Node(8, Node(7, None))), "Node(8, Node(7, None))")


def main():
    unittest.main()


if __name__ == '__main__':
    main()