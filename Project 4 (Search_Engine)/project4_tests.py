"""Test File for Project 4
   Parth Ray
"""

import unittest
from project4 import SearchEngine
from hashtables import import_stopwords, HashTableLinear, Pair


class TestCase(unittest.TestCase):
    def test_SE(self):
        SE = SearchEngine("docs",
                          import_stopwords("stop_words.txt", HashTableLinear()))
        self.assertEqual(SE.doc_length.num_items, 4)
        self.assertEqual(SE.stopwords,
                         import_stopwords("stop_words.txt", HashTableLinear()))
        self.assertEqual(SE.search("Computer Science")[0], Pair("docs\\test.txt", 1.0))
        self.assertEqual(SE.search("ADT")[0][0], "docs\\data_structure.txt")
        self.assertEqual(round(SE.search("ADT")[0][1], 2), 0.01)
        self.assertEqual(SE.search("Hash Table")[1][0], "docs\\data_structure.txt")
        self.assertEqual(round(SE.search("Hash Table")[1][1], 2), 0.01)
        list_of_pairs = [Pair("P", 5), Pair("A", 2), Pair("R", 1), Pair("T", 4), Pair("H", 3)]
        self.assertEqual(SE.rank(list_of_pairs),
                         [Pair("P", 5), Pair("T", 4), Pair("H", 3), Pair("A", 2), Pair("R", 1)])
        self.assertEqual(SE.get_scores(["computer", "science"])[0], Pair("docs\\test.txt", 1.0))
        self.assertEqual(SE.get_scores(["every", "nothing", "few"]), [])
        self.assertEqual(round(SE.get_wf(6), 2), 2.79)
        self.assertEqual(SE.get_wf(-6), 0)
        list1 = ["Automated information retrieval systems of ",
                 "Information retrieval and afterwards say\n"]
        list2 = ['automated', 'information', 'retrieval', 'systems', 'information', 'retrieval']
        self.assertEqual(SE.parse_words(list1), list2)
        self.assertEqual(SE.parse_words(["and afterwards say\n", "much without the"]), [])
        self.assertEqual(SE.read_file("docs\\test.txt"), ["computer science\n"])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
