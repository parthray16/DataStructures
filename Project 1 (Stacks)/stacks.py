"""Contains code for StackADTs
CPE202
Project 1

Author:
    Parth Ray
"""
from array_list import ArrayList
import array_list as alist
from linked_list import Node
import linked_list as llist

class StackArray:
    """Stack using array list
    Attributes:
        arr_list (ArrayList) : An array
        num_items (int) : number of items
    """
    def __init__(self):
        self.arr_list = ArrayList()
        self.num_items = 0

    def __repr__(self):
        return str(self.arr_list)

    def __eq__(self, other):
        return isinstance(other, StackArray) \
                and self.arr_list == other.arr_list \
                and self.num_items == other.num_items

    def is_empty(self):
        """method that tells if the stack is empty
        Args:
            No args
        Returns:
            boolean : True if StackArray is empty
        """
        return self.num_items == 0

    def push(self, item):
        """method that pushes (inserts) an item onto the stack
        Args:
            item (any type) : item to be pushed onto the stack
        Returns:
            None
        """
        self.arr_list = alist.insert(self.arr_list, item, self.num_items)
        self.num_items += 1

    def pop(self):
        """method that removes the item at the top of the stack
        Args:
            No args
        Returns:
            item (any type) : the item (data) that was removed
        Raises:
            IndexError : when the stack is empty
        """
        if self.is_empty():
            raise IndexError
        self.arr_list, item = alist.pop(self.arr_list, self.num_items - 1)
        self.num_items -= 1
        return item

    def peek(self):
        """method that tells us what the item at the top of the stack is
        Args:
            No args
        Returns:
            item (any type) : the item (data) at the top of the stack, without
                              removing it
        Raises:
            IndexError : when the stack is empty
        """
        if self.is_empty():
            raise IndexError
        return alist.get(self.arr_list, self.num_items - 1)

    def size(self):
        """method that gives the size of the stack
        Args:
            No args
        Returns:
            int : the number of items in the stack
        """
        return self.num_items

class StackLinked:
    """Stack using linked list
    Attributes:
        top (Node) : a linked list
        num_items (int) : number of items
    """

    def __init__(self):
        self.top = None
        self.num_items = 0

    def __repr__(self):
        return str(self.top)

    def __eq__(self, other):
        return isinstance(other, StackLinked) \
                and self.top == other.top \
                and self.num_items == other.num_items

    def is_empty(self):
        """method that tells if the stack is empty
        Args:
            No args
        Returns:
            boolean : True if StackLinked is empty
        """
        return self.num_items == 0

    def push(self, item):
        """method that pushes (inserts) an item onto the stack
        Args:
            item (any type) : item to be pushed onto the stack
        Returns:
            None
        """
        self.top = Node(item, self.top)
        self.num_items += 1

    def pop(self):
        """method that removes the item at the top of the stack
        Args:
            No args
        Returns:
            item (any type) : the item (data) that was removed
        Raises:
            IndexError : when the stack is empty
        """
        if self.is_empty():
            raise IndexError
        self.top, item = llist.pop(self.top, 0)
        self.num_items -= 1
        return item

    def peek(self):
        """method that tells us what the item at the top of the stack is
        Args:
            No args
        Returns:
            item (any type) : the item (data) at the top of the stack, without
                              removing it
        Raises:
            IndexError : when the stack is empty
        """
        if self.is_empty():
            raise IndexError
        return llist.get(self.top, 0)

    def size(self):
        """method that gives the size of the stack
        Args:
            No args
        Returns:
            int : the number of items in the stack
        """
        return self.num_items
