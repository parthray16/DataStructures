"""Lab 2
   Parth Ray"""

class Node:
    """Linked List is one of None or Node
    Attributes:
        val (int): an item in the list
        next (Node): a link to the next item in the list (Linked List)
    """
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return "Node(%d, %s)" % (self.val, self.next)

    def __eq__(self, other):
        return isinstance(other, Node) and self.val == other.val \
            and self.next == other.next

def insert(lst, val, pos):
    """inserts the integer at the position pos in the linked list recursively.
    Args:
        lst (Node): the list
        val (int): the value to be inserted in the list
        pos (int): the position
    Returns:
        Node: the head of a LinkedList
    Raises:
        IndexError: when the position is out of bound ( > num_items).
    """
    if pos == 0:
        return Node(val, lst)
    if pos < 0 or pos > size(lst):
        raise IndexError
    lst.next = insert(lst.next, val, pos - 1)
    return lst


def get(lst, pos):
    """gets an item stored at the specified position recursively.
    Args:
        lst (Node): a head of linked list
        pos (int): the specified position
    Returns:
        int: the val of the item at the position pos.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if pos == 0:
        return lst.val
    if pos < 0 or pos >= size(lst):
        raise IndexError
    return get(lst.next, pos - 1)


def search(lst, val):
    """searches for a specified value in a given list.
    Args:
        lst (Node): an object of Node (LinkedList)
        val (int): a value to search for
    Returns:
        int: the position where the value is stored in the list.
             It returns None if the value is not found.
    """
    return search_helper(lst, val, 0)


def search_helper(lst, val, pos):
    """a helper function to search for a specified value in a given list recursively
    Args:
        lst (Node) : an object of Node (LinkedList)
        val (str): a value to search for
        pos (int) : the current position in the list
    Returns:
        int : the position where the value is stored in the list.
              It returns None if the value is not found.
    """
    if lst is None:
        return None
    if val == lst.val:
        return pos
    return search_helper(lst.next, val, pos + 1)


def contains(lst, val):
    """checks if a specified value exists in a given list.
    This function calls search function.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        bool: True if the value is found or False if not.
    """
    if lst is None:
        return False
    if val == lst.val:
        return True
    return contains(lst.next, val)


def remove(lst, val):
    """removes the first occurrence of a specified value in a given list recursively.
    Args:
        lst (Node): the head of a LinkedList
        val (int): a value to be removed
    Returns:
        Node: the head of the linked list with the first occurrence of the value removed.
    """
    if lst is None:
        return None
    if val == lst.val:
        return lst.next
    lst.next = remove(lst.next, val)
    return lst


def pop(lst, pos):
    """removes the item at a specified position in a given list recursively
    Args:
        lst (Node): the head of a LinkedList
        pos (int): the position in the list where an item is removed
    Returns:
        Node: the head of the LinkedList with the item removed
        int: the removed item’s value.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if pos == 0:
        return lst.next, lst.val
    if pos < 0 or pos >= size(lst):
        raise IndexError
    lst.next, int_removed = pop(lst.next, pos - 1)
    return lst, int_removed


def size(lst):
    """returns the number of items stored in the LinkedList recursively.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        int: the number of items stored in the list
    """
    if lst is None:
        return 0
    return size_helper(lst.next, 1)


def size_helper(lst, num):
    """a helper function to find the number of items stored in the LinkedList recursively
    Args:
        lst (Node): an object of Node (LinkedList)
        num (int): a counter for the number of items stored in the list
    Returns:
        int: the number of items stored in the list
    """
    if lst is None:
        return num
    return size_helper(lst.next, num + 1)
