import unittest
from array_list import ArrayList
from array_list import enlarge
from array_list import shrink
from array_list import insert
from array_list import get
from array_list import search
from array_list import contains
from array_list import remove
from array_list import pop
from array_list import size

class TestCase(unittest.TestCase):
    def test_enlarge(self):
        lst1 = enlarge(ArrayList())
        lst2 = ArrayList()
        lst2.capacity = 4
        self.assertEqual(lst1.capacity, lst2.capacity)


    def test_shrink(self):
        lst1 = ArrayList()
        lst1.capacity = 6
        lst1 = shrink(lst1)
        self.assertEqual(lst1.capacity, 3)


    def test_insert(self):
        lst = ArrayList()
        self.assertEqual(insert(lst, 5, 0).arr, [5, None])
        lst.num_items = 4
        lst.capacity = 4
        lst.arr = [1, 2, 3, 4]
        self.assertEqual(insert(lst, 5, 2).arr, [1, 2, 5, 3, 4, None, None, None])
        self.assertRaises(IndexError, insert, lst, 20, 6)


    def test_get(self):
        lst = ArrayList()
        lst.num_items = 3
        lst.arr = [1, 2, 3]
        self.assertEqual(get(lst, 2), 3)
        self.assertEqual(get(lst, 1,), 2)
        self.assertRaises(IndexError, get, lst, 3)


    def test_search(self):
        lst = ArrayList()
        lst.num_items = 4
        lst.arr = [1, 2, 3, 20]
        self.assertEqual(search(lst, 3), 2)
        lst.arr = [70, 28, 1, 29]
        self.assertEqual(search(lst, 29), 3)
        self.assertEqual(search(lst, 2), None)


    def test_contains(self):
        lst = ArrayList()
        lst.num_items = 4
        lst.arr = [1, 2, 3, 4]
        self.assertTrue(contains(lst, 2))
        self.assertFalse(contains(lst, 5))
        self.assertTrue(contains(lst, 4))


    def test_remove(self):
        lst = ArrayList()
        self.assertEqual(remove(lst, 0), ArrayList())
        lst.arr = [1, 2, None, None]
        lst.capacity = 4
        lst.num_items = 2
        self.assertEqual(remove(lst, 2).arr, [1, None])
        lst.arr = [1, 2, 3, None]
        lst.capacity = 4
        lst.num_items = 3
        self.assertEqual(remove(lst, 2).arr, [1, 3, None, None])


    def test_pop(self):
        lst = ArrayList()
        lst.num_items = 2
        lst.arr = [1, 2]
        lst2 = ArrayList()
        lst2.num_items = 1
        lst2.arr = [1, None]
        self.assertEqual(pop(lst, 1), (lst2, 2))
        self.assertRaises(IndexError, pop, lst, 2)
        lst.arr = [1, 2, None, None]
        lst.capacity = 4
        lst.num_items = 2
        lst2.arr = [2, None]
        lst2.num_items = 1
        lst2.capacity = 2
        self.assertEqual(pop(lst, 0)[0].arr, [2, None])


    def test_size(self):
        lst1 = ArrayList()
        self.assertEqual(size(lst1), 0)
        lst1.num_items = 20
        self.assertEqual(size(lst1), 20)
        lst1.num_items = lst1.num_items // 5
        self.assertEqual(size(lst1), 4)


    def test_str(self):
        lst = ArrayList()
        lst.num_items = 4
        lst.arr = [1, 2, 3, 4]
        self.assertEqual(str(lst), "[1, 2, 3, 4]")


def main():
    unittest.main()


if __name__ == '__main__':
    main()