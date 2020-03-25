"""Lab 8 Test File
Parth Ray
"""
import unittest

from hashtables import (
    HashTableLinear, HashTableQuadratic, HashTableSepchain, Pair,
    import_stopwords)

class TestHash(unittest.TestCase):
    def test_hash_sepchain(self):
        table = HashTableSepchain()
        self.assertEqual(table.table_size, 11)
        table["3"] = "3"
        table["2"] = "2"
        table["4"] = "4"
        table["5"] = "5"
        self.assertEqual("5" in table, True)
        self.assertEqual("6" in table, False)
        self.assertRaises(KeyError, table.get, "6")
        table["3"] = "6"
        self.assertEqual(table["3"], "6")
        table[chr(40)] = "20"
        self.assertEqual(table["3"], "6")
        self.assertEqual(table.num_collisions, 1)
        table.remove("3")
        table.remove("4")
        self.assertRaises(KeyError, table.get, "4")
        self.assertRaises(KeyError, table.remove, "4")

    def test_hash_linear(self):
        table = HashTableLinear()
        self.assertEqual(table.table_size, 11)
        table["3"] = "3"
        table["2"] = "2"
        table["4"] = "4"
        table["5"] = "5"
        self.assertEqual("5" in table, True)
        self.assertEqual("6" in table, False)
        self.assertRaises(KeyError, table.get, "6")
        table["3"] = "6"
        self.assertEqual(table["3"], "6")
        table[chr(40)] = "20"
        self.assertEqual(table["3"], "6")
        self.assertEqual(table.num_collisions, 1)
        table.remove("3")
        table.remove("4")
        self.assertRaises(KeyError, table.get, "4")
        self.assertRaises(KeyError, table.remove, "4")

    def test_hash_quadratic(self):
        table = HashTableQuadratic()
        self.assertEqual(table.table_size, 11)
        table["3"] = "3"
        table["2"] = "2"
        table["4"] = "4"
        table["5"] = "5"
        self.assertEqual("5" in table, True)
        self.assertEqual("6" in table, False)
        self.assertRaises(KeyError, table.get, "6")
        table["3"] = "6"
        self.assertEqual(table["3"], "6")
        table[chr(40)] = "20"
        self.assertEqual(table["3"], "6")
        self.assertEqual(table.num_collisions, 1)
        table.remove("3")
        table.remove("4")
        self.assertRaises(KeyError, table.get, "4")
        self.assertRaises(KeyError, table.remove, "4")

    def test_import_stopwords(self):
        hashtable = import_stopwords("stop_words.txt", HashTableSepchain())
        self.assertEqual(hashtable["unless"], "unless")
        self.assertRaises(KeyError, hashtable.get, "Parth")
        hashtable = import_stopwords("stop_words.txt", HashTableLinear())
        self.assertEqual(hashtable["unless"], "unless")
        self.assertRaises(KeyError, hashtable.get, "Parth")
        hashtable = import_stopwords("stop_words.txt", HashTableQuadratic())
        self.assertEqual(hashtable["unless"], "unless")
        self.assertRaises(KeyError, hashtable.get, "Parth")

if __name__ == '__main__':
   unittest.main()
