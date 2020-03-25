"""Author: Parth Ray
   Lab 5

CPE202

Instructions:
    Complete this file by writing python3 code.

"""
import random
import bst
from classmate import Classmate, classmate_factory


class TreeMap:
    """a map that associates a key from a BST with its value
    Attributes:
        tree (BSTNode): a tree made up of BSTNodes
        num_items: number of items in the TreeMap
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        return str(self.tree)

    def __eq__(self, other):
        return isinstance(other, TreeMap) and \
                self.num_items == other.num_items and \
                self.tree == other.tree

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
           This function calls your get method.
        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            * : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.
        Args:
            key (*) : a key which is compareable by <,>,==
            val (*): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notation
        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)

    def put(self, key, val):
        """put a key value pair into the map, calls insert function in bst.py
        Args:
            key (*) : a key which is compareable by <,>,==
            val (*): the value associated with the key
        """
        self.tree = bst.insert(self.tree, key, val)
        self.num_items += 1

    def get(self, key):
        """put a key value pair into the map, calls get function in bst.py
        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            * : the value associated with the key
        """
        return bst.get(self.tree, key)

    def contains(self, key):
        """checks if a key exists within the tree, calls contains function in bst.py
        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return bst.contains(self.tree, key)

    def delete(self, key):
        """deletes a key and its associated value from tree, calls delete function in bst.py
        Args:
            key (*) : a key which is compareable by <,>,==
        """
        self.tree = bst.delete(self.tree, key)
        self.num_items -= 1

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self):
        """finds the value with the smallest key in the tree, calls find_min function in bst.py
        Returns:
            * : the smallest key in the tree
            * : the value associated with the smallest key in the tree
        """
        return bst.find_min(self.tree)

    def find_max(self):
        """finds the value with the largest key in the tree, calls find_max function in bst.py
        Returns:
            * : the largest key in the tree
            * : the value associated with the largest key in the tree
        """
        return bst.find_max(self.tree)

    def inorder_list(self):
        """method that gives a list of an inorder traversal of tree, calls inorder_list in bst.py
        Returns:
            list : a list of BST keys representing inorder traversal of BST
        """
        return bst.inorder_list(self.tree)

    def preorder_list(self):
        """method that gives a list of an preorder traversal of tree, calls preorder_list in bst.py
        Returns:
            list : a list of BST keys representing preorder traversal of BST
        """
        return bst.preorder_list(self.tree)

    def tree_height(self):
        """method that returns the tree height, calls tree_height in bst.py
        Returns:
            int : the height of the tree
        """
        return bst.tree_height(self.tree)

    def range_search(self, low, high):
        """method that returns a list of values that fall within the given range,
           calls range_search in bst.py
        Args:
            low (int): inclusive starting range value
            high (int): exclusive ending range value
        Returns:
            list : a list of values that fall within the given key range
        """
        return bst.range_search(self.tree, low, high)

def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is done for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    tree_map = TreeMap()
    classmates = []
    fpa = open(filename, "r")
    read_lines = fpa.readlines()
    classmates = [classmate_factory(i.split("\t")) for i in read_lines]
    fpa.close()
    random.seed(2)
    random.shuffle(classmates)
    for i in classmates:
        tree_map[i.sid] = i
    return tree_map


def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the student id as a key
    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : the id of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the id does not exist
    """
    if sid in tmap:
        return tmap[sid]
    raise KeyError("A classmate with the id: %d does not exist!" % (sid))
