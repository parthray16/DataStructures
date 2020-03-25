"""Author: Parth Ray
   Lab 10 RBTree

CPE202
"""
class RBTreeNode:
    """Node class for RBTree
    Attributes:
        key (*): a key that is comparable
        val (*): a value of any type
        left (RBTreeNode): left subtree
        right (RBTreeNode): right subtree
        color (str): color of RBTreeNode (red or black)
    """
    def __init__(self, color, key=None, val=None, left=None, right=None):
        self.right = right
        self.left = left
        self.key = key
        self.val = val
        self.color = color

    def __eq__(self, other):
        return isinstance(other, RBTreeNode) and \
                self.right == other.right and \
                self.left == other.left and \
                self.key == other.key and \
                self.val == other.val and \
                self.color == other.color

    def __repr__(self):
        return f"Tree({self.color}, {self.key}, {self.val}, {self.left}, {self.right})"


def get(tree, key):
    """a function that gets the value from a given key in a RBTree
    Args:
        tree (RBTreeNode): tree that is to be searched
        key (*): a key which is compareable by <,>,==
    Returns:
        val (*): the value associated with the key
    Raises:
        KeyError: when RBTree is empty or key not found
    """
    if tree is None:
        raise KeyError
    if key < tree.key:
        return get(tree.left, key)
    if key > tree.key:
        return get(tree.right, key)
    return tree.val


def contains(tree, key):
    """a function that tells if a given key is in RBTree
    Args:
        tree (RBTreeNode): tree that is to be searched
        key (*): a key which is compareable by <,>,==
    Returns:
        Boolean: True if key found in RBTree
    """
    if tree is None:
        return False
    if key < tree.key:
        return contains(tree.left, key)
    if key > tree.key:
        return contains(tree.right, key)
    return True


def insert(tree, key, val):
    """a function that inserts the value from a given key in a RBTree
    Args:
        tree (RBTreeNode): tree to put the inserted key and value into
        key (*): a key which is compareable by <,>,==
        val (*): the value associated with the key
    Returns:
        RBTreeNode: the tree witht the inserted key value pair
    """
    tree = insert_helper(tree, key, val)
    tree.color = 'black'
    return tree

def insert_helper(tree, key, val):
    """a helper function that inserts the value from a given key in a RBTree
    Args:
        tree (RBTreeNode): tree to put the inserted key and value into
        key (*): a key which is compareable by <,>,==
        val (*): the value associated with the key
    Returns:
        RBTreeNode: the tree witht the inserted key value pair
    """
    if tree is None:
        return RBTreeNode('red', key, val)
    if key == tree.key:
        tree.val = val
    elif key < tree.key:
        tree.left = insert_helper(tree.left, key, val)
    else:
        tree.right = insert_helper(tree.right, key, val)
    return rebalance(tree)

def rebalance(tree):
    """Rebalance the tree so that the property of the RB Tree is maintained.
        If the subtree matches one of the 4 patterns,
        it will convert the subtree to BRB
    Args:
        tree (RBTreeNode): a Red Black Tree
    Returns:
        RBTreeNode : a Red Black Tree
    """
    #RRB
    if tree.color == 'black' and tree.left and tree.left.color == 'red' and \
       tree.left.left and tree.left.left.color == 'red':
        return  RBTreeNode('red', tree.left.key, tree.left.val,
                           RBTreeNode('black', tree.left.left.key, tree.left.left.val,
                                      tree.left.left.left, tree.left.left.right),
                           RBTreeNode('black', tree.key, tree.val, tree.left.right, tree.right))
    #R RB
    if tree.color == 'black' and tree.left and tree.left.color == 'red' and \
        tree.left.right and tree.left.right.color == 'red':
        return  RBTreeNode('red', tree.left.right.key, tree.left.right.val,
                           RBTreeNode('black', tree.left.key, tree.left.val,
                                      tree.left.left, tree.left.right.left),
                           RBTreeNode('black', tree.key, tree.val,
                                      tree.left.right.right, tree.right))
    #BR R
    if tree.color == 'black' and tree.right and tree.right.color == 'red' and \
        tree.right.left and tree.right.left.color == 'red':
        return  RBTreeNode('red', tree.right.left.key, tree.right.left.val,
                           RBTreeNode('black', tree.key, tree.val, tree.left, tree.right.left.left),
                           RBTreeNode('black', tree.right.key, tree.right.val,
                                      tree.right.left.right, tree.right.right))
    #BRR
    if tree.color == 'black' and tree.right and tree.right.color == 'red' and \
        tree.right.right and tree.right.right.color == 'red':
        return  RBTreeNode('red', tree.right.key, tree.right.val,
                           RBTreeNode('black', tree.key, tree.val, tree.left, tree.right.left),
                           RBTreeNode('black', tree.right.right.key, tree.right.right.val,
                                      tree.right.right.left, tree.right.right.right))
    return tree

def delete(tree, key):
    """a function that deletes the key and its value from a RBTree
    Args:
        tree (RBTreeNode): tree to delete the key and value from
        key (*): a key which is compareable by <,>,==
    Returns:
        RBTreeNode: tree without the key value pair
    Raises:
        KeyError: when RBTree is empty or key is not found
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
        tree (RBTreeNode): subtree to get replacment from
    Returns:
        RBTreeNode: replacment RBTreeNode for deleted RBTreeNode
    Raises:
        ValueError: when subtree is empty
    """
    if tree is None:
        raise ValueError
    if tree.left is None:
        return tree
    return get_rep(tree.left)


def find_min(tree):
    """a function that finds the smallest key in a RBTree
    Args:
        tree (RBTreeNode): RBTree that you want smallest key from
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
    """a function that finds the largest key in a RBTree
    Args:
        tree (RBTreeNode): RBTree that you want largest key from
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
    """a function that gives a list of keys a RBTree read inorder
    Args:
        tree (RBTreeNode): tree that is to be read
    Returns:
        list: list of keys from tree read inorder
    """
    return inorder_list_helper(tree, [])

def inorder_list_helper(tree, accum):
    """helper function that gives a list of keys a RBTree read inorder
    Args:
        tree (RBTreeNode): tree that is to be read
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
    """a function that gives a list of keys a RBTree read preorder
    Args:
        tree (RBTreeNode): tree that is to be read
    Returns:
        list: list of keys from tree read preorder
    """
    return preorder_list_helper(tree, [])

def preorder_list_helper(tree, accum):
    """helper function that gives a list of keys a RBTree read preorder
    Args:
        tree (RBTreeNode): tree that is to be read
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
    """function that gives height of a RBTree
    Args:
        tree (RBTreeNode): tree that you want height of
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
    """a function that gets range of keys from RBTree
    Args:
        tree (RBTreeNode): tree that you want range from
        low (int): inclusive starting range value
        high (int): exclusive ending range value
    Returns:
        list : a list of values that fall within the given key range
    """
    return range_search_helper(tree, low, high, [])

def range_search_helper(tree, low, high, accum):
    """helper function that gets range of keys from RBTree
    Args:
        tree (RBTreeNode): tree that you want range from
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

def draw_tree(tree):
    if tree is None:
        raise isEmptyError
    if tree.left and tree.right:
        write tree pointing to both left and right
    if tree.left:
        write tree pointing to left
    if tree.right:
        write tree pointing to right
    if tree.left is None and tree.right is None:
        write tree
    