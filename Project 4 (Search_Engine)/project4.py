"""CPE 202 Project 4 Search Engine
Author: Parth Ray
"""

import sys
import os
import math
from hashtables import HashTableLinear, import_stopwords, Pair, keys


def main():
    """It  takes a directory name as its command line argument and continuously askes for
       user input on what query terms to search for. It will return the relavent files
       associated with the query terms or inputing q will exit the function and return None
    """
    search_engine = SearchEngine(sys.argv[1], import_stopwords("stop_words.txt", HashTableLinear()))
    while True:
        user_input = input("Type 's:' and what you would like to search for or type 'q' to exit: ")
        if user_input == "q":
            return
        if "s:" in user_input:
            user_input = user_input[2::].lower().strip()
            print(search_engine.search(user_input))

class SearchEngine:
    """Builds and maintains an inverted index of documents stored in a specified directory and
       provides a functionality to search documents with query terms
    Attributes:
        directory (str): a directory name
        stopwords (HashMap): a hash table containing stopwords
        doc_length (HashMap) : a hash table containing the total number of words in each document
        term_freqs (HashMap) : a hash table of hash tables for each term. Each hash table
                               contains the frequency of the term in documents
    """
    def __init__(self, directory, stopwords):
        self.doc_length = HashTableLinear()
        self.term_freqs = HashTableLinear()
        self.stopwords = stopwords
        self.index_files(directory)

    def __eq__(self, other):
        return isinstance(other, SearchEngine) \
                and self.doc_length == other.doc_length \
                and self.term_freqs == other.term_freqs \
                and self.stopwords == other.stopwords \

    def __repr__(self):
        return f"SearchEngine({self.doc_length}, {self.term_freqs})"


    def read_file(self, infile):
        """A helper function to read a file
        Args:
            infile (str) : the path to a file
        Returns:
            list : a list of str read from a file
        """
        with open(infile, "r") as item:
            return item.readlines()

    def parse_words(self, lines):
        """split strings into words, convert words to lower cases and remove new line chars.
           Exclude stopwords.
        Args:
            lines (list) : a list of strings
        Returns:
            list : a list of words
        """
        list_of_words = []
        for i in lines:
            list_of_strings = i.split()
            for j in list_of_strings:
                j = j.lower().strip()
                if not j in self.stopwords:
                    list_of_words.append(j)
        return list_of_words

    def count_words(self, filename, words):
        """count words in a file and store the frequency of each
           word in the term_freqs hash table. Words should not contain stopwords.
           Also store the total count of words contained in the file in the doc_length hash table.
        Args:
            filename (str) : the file name
            words (list) : a list of words
        """
        self.doc_length[filename] = len(words)
        for i in words:
            if not i in self.term_freqs:
                self.term_freqs[i] = HashTableLinear()
            if filename in self.term_freqs[i]:
                self.term_freqs[i][filename] += 1
            else:
                self.term_freqs[i][filename] = 1

    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str) : the path of a directory
        """
        list_of_files = os.listdir(directory)
        for i in list_of_files:
            item = os.path.join(directory, i)
            if os.path.isfile(item):
                parts = os.path.splitext(item)
                if parts[1] == ".txt":
                    self.count_words(item, self.parse_words(self.read_file(item)))

    def get_wf(self, term_freq):
        """computes the weighted frequency
        Args:
            term_freq (float) : term frequency
        Returns:
            float : the weighted frequency
        """
        if term_freq > 0:
            wfreq = 1 + math.log(term_freq)
        else:
            wfreq = 0
        return wfreq

    def get_scores(self, terms):
        """creates a list of scores for each file in corpus
           The score = weighted frequency / the total word count in the file.
           Compute this score for each term in a query and sum all the scores.
        Args:
            terms (list) : a list of str
        Returns:
            list : a list of Pairs, each containing the filename and its relevancy score
        """
        scores = HashTableLinear()
        for query in terms:
            if query in self.term_freqs:
                term_hash = self.term_freqs[query]
                for i in term_hash.table:
                    if i:
                        if not i.key in scores:
                            scores[i.key] = 0
                        scores[i.key] += self.get_wf(i.data)
        for j in range(len(scores.table)):
            if scores.table[j]:
                scores.table[j].data /= self.doc_length[scores.table[j].key]
            else:
                scores.table[j] = Pair(None, 0)
        return keys(scores)

    def rank(self, scores):
        """ranks files in the descending order of relevancy
        Args:
            scores(list) : a list of Pairs: (filename, score)
        Returns:
            list : a list of tuples: (filename, score) sorted in descending order of relevancy
        """
        for i in range(len(scores)):
            max_idx = i
            for j in range(i + 1, len(scores)):
                if scores[j][1] > scores[max_idx][1]:
                    max_idx = j
            scores[i], scores[max_idx] = scores[max_idx], scores[i]
        return scores

    def search(self, query):
        """ search for the query terms in files
        Args:
            query (str) : query input
        Returns:
            list : list of files in descending order or relevancy
        """
        terms = self.parse_words([query])
        return self.rank(self.get_scores(terms))

if __name__ == '__main__':
    main()
