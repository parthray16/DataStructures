"""Module for BST
   CPE202

Contains the data definition of BST,
and functions (not class member methods) on BST.

Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.

Author:
    Section: 5
    Parth Ray
"""
class BSTNode:
    """Node class for BST
    Attributes:
        key (*): a key that is comparable
        val (*): a value of any type
        left (BSTNode): left subtree
        right (BSTNode): right subtree
    """
    def __init__(self):
        self.right = None
        self.left = None
        self.key = None
        self.val = None

    def __eq__(self, other):
        return isinstance(other, BSTNode) and \
                self.right == other.right and \
                self.left == other.left and \
                self.key == other.key and \
                self.val == other.val

    def __repr__(self):
        return f"Tree({self.key}, {self.val}, {self.left}, {self.right})"


def get(tree, key):
    """a function that gets the value from a given key in a BST
    Args:
        tree (BSTNode): tree that is to be searched
        key (*): a key which is compareable by <,>,==
    Returns:
        val (*): the value associated with the key
    Raises:
        KeyError: when BST is empty or key not found
    """
    if tree is None:
        raise KeyError
    if key < tree.key:
        return get(tree.left, key)
    if key > tree.key:
        return get(tree.right, key)
    return tree.val


def contains(tree, key):
    """a function that tells if a given key is in BST
    Args:
        tree (BSTNode): tree that is to be searched
        key (*): a key which is compareable by <,>,==
    Returns:
        Boolean: True if key found in BST
    """
    if tree is None:
        return False
    if key < tree.key:
        return contains(tree.left, key)
    if key > tree.key:
        return contains(tree.right, key)
    return True


def insert(tree, key, val):
    """a function that inserts the value from a given key in a BST
    Args:
        tree (BSTNode): tree to put the inserted key and value into
        key (*): a key which is compareable by <,>,==
        val (*): the value associated with the key
    Returns:
        BSTNode: the tree with the inserted key value pair
    """
    if tree is None:
        node = BSTNode()
        node.key, node.val = key, val
        return node
    if key == tree.key:
        tree.val = val
    elif key < tree.key:
        tree.left = insert(tree.left, key, val)
    else:
        tree.right = insert(tree.right, key, val)
    return tree


def delete(tree, key):
    """a function that deletes the key and its value from a BST
    Args:
        tree (BSTNode): tree to delete the key and value from
        key (*): a key which is compareable by <,>,==
    Returns:
        BSTNode: tree without the key value pair
    Raises:
        KeyError: when BST is empty or key is not found
    """
    if tree is None:
        raise KeyError
    if tree.key == key:
        if tree.left and tree.right:
            rep = get_rep(tree.right)
            tree = delete(tree, rep.key)
            tree.key, tree.val = rep.key, rep.val
            return tree
        if tree.left:
            return tree.left
        return tree.right
    if tree.key > key:
        tree.left = delete(tree.left, key)
    else:
        tree.right = delete(tree.right, key)
    return tree


def get_rep(tree):
    """a function that gets the right neighbor value and key for delete function
    Args:
        tree (BSTNode): subtree to get replacment from
    Returns:
        BSTNode: replacment BSTNode for deleted BSTNode
    Raises:
        ValueError: when subtree is empty
    """
    if tree is None:
        raise ValueError
    if tree.left is None:
        return tree
    return get_rep(tree.left)


def find_min(tree):
    """a function that finds the smallest key in a BST
    Args:
        tree (BSTNode): BST that you want smallest key from
    Returns:
        key (*): smallest key in tree
        val (*): the value associated with the key
    """
    if tree is None:
        return None, None
    if tree.left is None:
        return tree.key, tree.val
    return find_min(tree.left)


def find_max(tree):
    """a function that finds the largest key in a BST
    Args:
        tree (BSTNode): BST that you want largest key from
    Returns:
        key (*): largest key in tree
        val (*): the value associated with the key
    """
    if tree is None:
        return None, None
    if tree.right is None:
        return tree.key, tree.val
    return find_max(tree.right)


def inorder_list(tree):
    """a function that gives a list of keys a BST read inorder
    Args:
        tree (BSTNode): tree that is to be read
    Returns:
        list: list of keys from tree read inorder
    """
    return inorder_list_helper(tree, [])

def inorder_list_helper(tree, accum):
    """helper function that gives a list of keys a BST read inorder
    Args:
        tree (BSTNode): tree that is to be read
        accum (list): empty list to add keys
    Returns:
        list: list of keys from tree read inorder
    """
    if tree is None:
        return accum
    inorder_list_helper(tree.left, accum)
    accum.append(tree.key)
    inorder_list_helper(tree.right, accum)
    return accum


def preorder_list(tree):
    """a function that gives a list of keys a BST read preorder
    Args:
        tree (BSTNode): tree that is to be read
    Returns:
        list: list of keys from tree read preorder
    """
    return preorder_list_helper(tree, [])

def preorder_list_helper(tree, accum):
    """helper function that gives a list of keys a BST read preorder
    Args:
        tree (BSTNode): tree that is to be read
        accum (list): empty list to add keys
    Returns:
        list: list of keys from tree read preorder
    """
    if tree is None:
        return accum
    accum.append(tree.key)
    preorder_list_helper(tree.left, accum)
    preorder_list_helper(tree.right, accum)
    return accum


def tree_height(tree):
    """function that gives height of a BST
    Args:
        tree (BSTNode): tree that you want height of
    Returns:
        int : height of tree
    """
    if tree is None:
        return -1
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    height = max(left_height, right_height) + 1
    return height


def range_search(tree, low, high):
    """a function that gets range of keys from BST
    Args:
        tree (BSTNode): tree that you want range from
        low (int): inclusive starting range value
        high (int): exclusive ending range value
    Returns:
        list : a list of values that fall within the given key range
    """
    return range_search_helper(tree, low, high, [])

def range_search_helper(tree, low, high, accum):
    """helper function that gets range of keys from BST
    Args:
        tree (BSTNode): tree that you want range from
        low (int): inclusive starting range value
        high (int): exclusive ending range value
        accum (list): empty list to add values to
    Returns:
        list : a list of values that fall within the given key range
    """
    if tree is None:
        return accum
    if tree.key < low:
        range_search_helper(tree.right, low, high, accum)
    elif tree.key >= high:
        range_search_helper(tree.left, low, high, accum)
    else:
        range_search_helper(tree.left, low, high, accum)
        accum.append(tree.val)
        range_search_helper(tree.right, low, high, accum)
    return accum
