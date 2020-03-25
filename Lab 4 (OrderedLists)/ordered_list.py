"""CPE 202
   Lab 4
   Parth Ray
"""
class Node:
    """ A node of a list
    Attributes:
        val (int): the payload
        next (Node): the next item in the list
        prev (Node): the previous item in the list
    """
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        return f"Node({self.val}, {self.next})"

    def __eq__(self, other):
        return isinstance(other, Node) \
                and self.val == other.val \
                and self.next == other.next \
                and self.prev == other.prev

class OrderedList:
    """an ordered list
    Attributes:
        head (Node): a ponter to the head of the list
        tail (Node): a pointer to the tail of the list
        num_items (int): the number of items stored in the list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __eq__(self, other):
        return isinstance(other, OrderedList) \
                and self.head == other.head \
                and self.tail == other.tail \
                and self.num_items == other.num_items

    def __repr__(self):
        return str(self.head)

    def add(self, item):
        """adds a specified value as an item in the list while maintaining ascending order.
        Args:
            item (int): a value to be added as an item in the list
        """
        item = Node(val=item)
        if self.head is None:
            self.head = item
            self.tail = self.head
            self.num_items += 1
        elif item.val < self.head.val:
            self.head.prev = item
            item.next = self.head
            self.head = item
            self.num_items += 1
        elif item.val > self.tail.val:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
            self.num_items += 1
        else:
            cur = self.head
            while cur is not None and cur.val <= item.val:
                cur = cur.next
            next1 = cur
            prev1 = cur.prev
            prev1.next = item
            item.prev = prev1
            next1.prev = item
            item.next = next1
            self.num_items += 1

    def remove(self, item):
        """removes the first occurrence of a specified value in the list while maintaining
           ascending order.
        Args:
            item (int): a value to be removed
        Returns:
            int: the position where the item removed
        Raises:
            ValueError: when the item is not found in the list
        """
        self.head, self.tail, pos = self.remove_helper(self.head, self.tail, item, 0)
        self.num_items -= 1
        return pos

    def remove_helper(self, head, tail, item, pos):
        """helper that removes the first occurrence of a specified value in the list while
           maintaining ascending order and sets new head and tail pointers
        Args:
            head (Node): pointer to the front of an ordered list
            tail (Node): pointer to the end of an ordered list
            item (int): a value to be removed
            pos (int): counter for position of item removed
        Returns:
            Node: the new head of the list
            Node: the new tail of the list
            int: the position where the item removed
        Raises:
            ValueError: when the item is not found in the list or list is empty
        """
        if head is None or self.is_empty():
            raise ValueError
        if head.val == item:
            if self.num_items == 1:
                return None, None, 0
            if head.next is None:
                return head.next, head.prev, pos
            head.next.prev = head.prev
            return head.next, tail, pos
        head.next, tail, pos = self.remove_helper(head.next, tail, item, pos + 1)
        return head, tail, pos

    def search_forward(self, item):
        """searches a specified item in the list starting from the head.
        Args:
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        return self.search_forward_helper(self.head, item)

    def search_forward_helper(self, node, item):
        """helper that searches a specified item in the list starting from the head
        Args:
            node (Node): the head of the list
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        if node is None:
            return False
        if node.val == item:
            return True
        return self.search_forward_helper(node.next, item)

    def search_backward(self, item):
        """searches a specified item in the list backward starting from the tail.
        Args:
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        return self.search_backward_helper(self.tail, item)

    def search_backward_helper(self, tail, item):
        """helper that searches a specified item in the list starting from the tail
        Args:
            node (Node): the tail of the list
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        if tail is None:
            return False
        if tail.val == item:
            return True
        return self.search_backward_helper(tail.prev, item)

    def is_empty(self):
        """checks if the list is empty.
        Returns:
            bool: True if it is empty, False otherwise.
        """
        return self.num_items == 0

    def size(self):
        """gets the number of items stored in the list.
        Returns:
            int: the number of items in the list.
        """
        return self.num_items

    def index(self, item):
        """gets the position of the first occurrence of a specified item in the list.
        Args:
            item (int): the value to be found
        Returns:
            int: the position in the list
        Raises:
            LookupError: if the value is not found in the list
        """
        return self.index_helper(self.head, item)

    def index_helper(self, node, item):
        """helper that gets the position of the first occurrence of a specified
           item in the list.
        Args:
            node (Node): the head of a list
            item (int): the value to be found
        Returns:
            int: the position in the list
        Raises:
            LookupError: if the value is not found in the list
        """
        if node is None:
            raise LookupError
        if node.val == item:
            return 0
        return 1 + self.index_helper(node.next, item)

    def pop(self, pos=None):
        """removes the item at a specified position and returns its value.
        The last item in the list is removed if the argument is not passed.

        Args:
            pos (int): the position of the item to be removed. The default value is None
        Returns:
            int: the value of the item that is removed
        Raises:
            IndexError: if the position is out of bound
        """
        self.head, self.tail, item = self.pop_helper(self.head, self.tail, pos)
        self.num_items -= 1
        return item

    def pop_helper(self, head, tail, pos):
        """helper method for pop that removes the item at a position and sets new
           values for the head and tail pointers
        Args:
            head (Node): pointer to the front of an ordered list
            tail (Node): pointer to the end of an ordered list
            pos (int): the position of the item to be removed. The default value is None.
                       If None remove the last item.
        Returns:
            Node: the new head of the list
            Node: the new tail of the list
            int: the value that was removed
        Raises:
            IndexError: if the position is out of bound or OrderedList is empty
        """
        if self.is_empty():
            raise IndexError
        if pos is None:
            if self.num_items == 1:
                return None, None, head.val
            tail.prev.next = None
            return head, tail.prev, tail.val
        if pos >= self.size():
            raise IndexError
        if pos <= (self.size() / 2):
            if pos == 0:
                if self.num_items == 1:
                    return None, None, head.val
                head.next.prev = head.prev
                return head.next, tail, head.val
            head.next, tail, item = self.pop_helper(head.next, tail, pos - 1)
            return head, tail, item
        if pos == 0:
            tail.prev.next = tail.next
            return head, tail.prev, head.val
        head, tail.prev, item = self.pop_helper(head, tail.prev, pos - 1)
        return head, tail, item
