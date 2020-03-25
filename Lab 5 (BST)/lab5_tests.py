"""Test File for Lab 5 and BST
   Parth Ray
"""

import unittest
from bst import *
from lab5 import *


class TestCase(unittest.TestCase):
    def test_get(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        self.assertEqual(get(tree, 4), "P")
        self.assertEqual(get(tree, 3), "A")
        self.assertEqual(get(tree, 5), "R")
        self.assertRaises(KeyError, get, None, 4)

    def test_contains(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        self.assertEqual(contains(tree, 5), True)
        self.assertEqual(contains(tree, 7), False)

    def test_insert(self):
        tree = None
        tree1 = BSTNode()
        tree1.key, tree1.val = 3, "P"
        self.assertEqual(insert(tree, 3, "P"), tree1)

    def test_delete(self):
        self.assertRaises(KeyError, delete, None, 4)
        tree = insert(None, 4, "P")
        self.assertEqual(delete(tree, 4), None)
        tree = insert(tree, 3, "A")
        tree = insert(tree, 8, "R")
        tree = insert(tree, 7, "T")
        tree = insert(tree, 0, "H")
        tree = insert(tree, 9, "R")
        tree1 = insert(None, 4, "P")
        tree1 = insert(tree, 3, "A")
        tree1 = insert(tree, 9, "R")
        tree1 = insert(tree, 7, "T")
        tree1 = insert(tree, 0, "H")
        self.assertEqual(delete(tree, 8), tree1)

    def test_find_min(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        tree = insert(tree, 7, "T")
        tree = insert(tree, 0, "H")
        self.assertEqual(find_min(tree), (0, "H"))

    def test_find_max(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        tree = insert(tree, 7, "T")
        tree = insert(tree, 0, "H")
        self.assertEqual(find_max(tree), (7, "T"))

    def test_inorder_list(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        self.assertEqual(inorder_list(tree), [3, 4, 5])

    def test_preorder_list(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        self.assertEqual(preorder_list(tree), [4, 3, 5])

    def test_tree_height(self):
        tree = insert(None, 4, "P")
        self.assertEqual(tree_height(tree), 0)
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        self.assertEqual(tree_height(tree), 1)
        tree = insert(tree, 2, "T")
        tree = insert(tree, 1, "H")
        tree = insert(tree, 0, "R")
        self.assertEqual(tree_height(tree), 4)

    def test_range_search(self):
        tree = insert(None, 4, "P")
        tree = insert(tree, 3, "A")
        tree = insert(tree, 5, "R")
        tree = insert(tree, 7, "T")
        tree = insert(tree, 0, "H")
        self.assertEqual(range_search(tree, 0, 5), ["H", "A", "P"])
        self.assertEqual(range_search(tree, 0, 10), ["H", "A", "P", "R", "T"])
        self.assertEqual(range_search(tree, 7, 10), ["T"])

    def test_tmap(self):
        tmap = TreeMap()
        self.assertRaises(KeyError, tmap.get, 5)
        tmap[4] = "four"
        tmap[3] = "three"
        tmap[5] = "five"
        self.assertEqual(tmap.get(5), "five")
        self.assertEqual(tmap.contains(5), True)
        self.assertEqual(tmap.contains(7), False)
        self.assertEqual(tmap.size(), 3)
        self.assertEqual(tmap.find_min(), (3, "three"))
        self.assertEqual(tmap.find_max(), (5, "five"))
        self.assertEqual(tmap.inorder_list(), [3, 4, 5])
        self.assertEqual(tmap.preorder_list(), [4, 3, 5])
        self.assertEqual(tmap.tree_height(), 1)
        self.assertEqual(tmap.range_search(3, 5), ["three", "four"])

    def test_classmates(self):
        tmap = import_classmates("2202-cpe202-05.tsv")
        self.assertEqual(search_classmate(tmap, 25), Classmate(25, "Ray", "Parth D.", "CSC",
                                                               "Junior"))
        self.assertRaises(KeyError, search_classmate, tmap, 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
