"""
CPE202
Lab 7 Test File
Min PQ
Author:
    Parth Ray
"""
import unittest
from min_pq import MinPQ

class TestCase(unittest.TestCase):
    def test_min_pq(self):
        minq = MinPQ([5, 4, 3, 2, 1, 0])
        minq2 = MinPQ()
        minq2.insert(0)
        minq2.insert(1)
        self.assertEqual(minq2.capacity, 2)
        minq2.insert(2)
        self.assertEqual(minq2.capacity, 4)
        minq2.insert(3)
        minq2.insert(4)
        minq2.insert(5)
        self.assertEqual(minq2.min(), 0)
        minq2.del_min()
        self.assertEqual(minq2.min(), 1)
        self.assertEqual(minq2.size(), 5)
        minq2.del_min()
        minq2.del_min()
        self.assertEqual(minq2.capacity, 8)
        minq2.del_min()
        self.assertEqual(minq2.capacity, 4)
        minq2.del_min()
        minq2.del_min()
        self.assertRaises(IndexError, minq2.del_min)

def main():
    unittest.main()

if __name__ == "__main__":
    main()