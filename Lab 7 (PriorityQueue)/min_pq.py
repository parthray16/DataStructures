"""Minimum Priority Queue
For:
    CPE202
    Sections 3 & 5
    Winter 2020
Author:
    Parth Ray
"""
class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): the capacity of the queue. The default capacity is 2,
                        but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, arr=None):
        if arr is None:
            self.capacity = 2
            self.arr = [None] * self.capacity
            self.num_items = 0
        else:
            self.capacity = len(arr)
            self.num_items = len(arr)
            self.arr = self.heapify(arr)

    def __eq__(self, other):
        return isinstance(other, MinPQ) and \
                self.num_items == other.num_items and \
                self.capacity == other.capacity and \
                self.arr == other.arr

    def __repr__(self):
        if self.num_items == 0:
            return "[]"
        string = "["
        for i in range(self.num_items - 1):
            string += str(self.arr[i]) + ", "
        return string + str(self.arr[self.num_items - 1]) + "]"


    def heapify(self, arr):
        """initialize the queue with a given array and convert the array into a min heap
        Args:
            arr (list): an array
        Returns:
            list: array in min heap order
        """
        self.arr = arr
        i = self.index_parent(self.num_items - 1)
        while i >= 0:
            self.shift_down(i)
            i -= 1
        return self.arr


    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.
        Args:
            item (any): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
        """
        if self.capacity == self.num_items:
            self.enlarge()
        self.arr[self.num_items] = item
        self.shift_up(self.num_items)
        self.num_items += 1


    def del_min(self):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array

        Returns:
            any : it returns the minimum item, which has just been deleted
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.is_empty():
            raise IndexError
        min_val = self.arr[0]
        self.arr[0], self.arr[self.num_items - 1] = self.arr[self.num_items - 1], None
        self.num_items -= 1
        self.shift_down(0)
        if self.capacity > 2 and self.num_items > 0 and (4 * self.num_items <= self.capacity):
            self.shrink()
        return min_val


    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
            any : it returns the minimum item
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.is_empty():
            raise IndexError
        return self.arr[0]


    def is_empty(self):
        """checks if the queue is empty
        Returns:
            bool : True if empty, False otherwise.
        """
        return self.num_items == 0


    def size(self):
        """returns the number of items in the queue
        Returns:
            int : it returns the number of items in the queue
        """
        return self.num_items


    def enlarge(self):
        """enlarges the array.
        """
        self.capacity = self.capacity * 2
        self.arr = self.arr + [None] * len(self.arr)


    def shrink(self):
        """shrinks the array.
        """
        self.capacity = self.capacity // 2
        self.arr = self.arr[0:len(self.arr)//2]


    def shift_up(self, idx):
        """shifts up an item in the queue using tail recursion.
        Args:
            idx (int): the index of the item to be shifted up in the array.
        Returns:
            None : it returns nothing
        """
        parent = self.index_parent(idx)
        if parent < 0 or self.arr[parent] < self.arr[idx]:
            return None
        self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
        return self.shift_up(parent)


    def shift_down(self, idx):
        """shifts down an item in the queue using tail recursion.
        Args:
            idx (int): the index of the item to be shifted down in the array.
        Returns:
            None : it returns nothing
        """
        idx_min = self.index_minchild(idx, self.num_items - 1)
        if idx_min < 0 or self.arr[idx] < self.arr[idx_min]:
            return None
        self.arr[idx_min], self.arr[idx] = self.arr[idx], self.arr[idx_min]
        return self.shift_down(idx_min)


    def index_left(self, idx):
        """returns the index of the left child
        Args:
            idx (int): the index of the node
        Returns:
            int : it returns the index of the left child
        """
        return 2 * idx + 1


    def index_right(self, idx):
        """returns the index of the right child
        Args:
            idx (int): the index of the node
        Returns:
            int : it returns the index of the right child
        """
        return 2 * idx + 2


    def index_parent(self, idx):
        """returns the index of the parent
        Args:
            idx (int): the index of the node
        Returns:
            int : it returns the index of the parent
        """
        return (idx - 1) // 2


    def index_minchild(self, idx, end):
        """returns the index of the min child
        Args:
            idx (int): the index of the node
            end (int): the end index of the heap
        Returns:
            int : it returns the index of the min child
        """
        left = self.index_left(idx)
        right = self.index_right(idx)
        if left == end:
            return left
        if left > end or right > end or idx < 0:
            return -1
        if self.arr[left] < self.arr[right]:
            return left
        return right
