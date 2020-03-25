"""Starter code for Lab 3
CPE202

Parth Ray
"""
from linked_list import Node


class QueueArray:
    """Queue using Array List
    Attributes:
        capacity (int): the maximum number of items that can be stored in queue
        front (int): pointer to the front of queue
        rear (int): pointer to the rear of queue
        items (list): array whose size is the capacity
        num_items (int): the number of items in array
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.items = [None] * (self.capacity + 1)
        self.num_items = 0

    def __eq__(self, other):
        return isinstance(other, QueueArray) \
                and self.capacity == other.capacity \
                and self.front == other.front \
                and self.rear == other.rear \
                and self.num_items == other.num_items \
                and self.items == other.items

    def __repr__(self):
        return self.items

    def is_empty(self):
        """method that tells if queue is empty or not
        Args:
            No args
        Returns:
            Boolean: True if number of items is zero
        """
        return self.num_items == 0

    def is_full(self):
        """method that tells if queue is full or not
        Args:
            No args
        Returns:
            Boolean: True if rear is one index behind front
        """
        return self.front == (self.rear + 1) % len(self.items)

    def enqueue(self, item):
        """method that adds an item to the queue
        Args:
            item (any type): item that is to be added to queue
        Returns:
            None
        """
        if self.is_full():
            raise IndexError
        self.items[self.rear] = item
        self.rear += 1
        self.rear %= len(self.items)
        self.num_items += 1

    def dequeue(self):
        """method that removes the item in front of the queue
        Args:
            No args
        Returns:
            Data (any type): the data that was first in queue
        """
        if self.is_empty():
            raise IndexError
        val = self.items[self.front]
        self.front += 1
        self.front %= len(self.items)
        self.num_items -= 1
        return val

    def size(self):
        """method that gives number of items in stack
        Args:
            No args
        Returns:
            int: the number of items stored in the queue
        """
        return self.num_items


class QueueLinked:
    """Queue using Linked List
    Attributes:
        capacity (int): the maximum number of items that can be stored in queue
        front (Node): pointer to the front of queue
        rear (Node): pointer to the rear of queue
        num_items (int): the number of items in array
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.num_items = 0

    def __eq__(self, other):
        return isinstance(other, QueueLinked) \
                and self.capacity == other.capacity \
                and self.front == other.front \
                and self.rear == other.rear \
                and self.num_items == other.num_items

    def __repr__(self):
        return str(self.front)

    def is_empty(self):
        """method that tells if queue is empty or not
        Args:
            No args
        Returns:
            Boolean: True if number of items is zero
        """
        return self.num_items == 0 and self.front is None and self.rear is None

    def is_full(self):
        """method that tells if queue is full or not
        Args:
            No args
        Returns:
            Boolean: True if number of items is equal to capacity
        """
        return self.num_items == self.capacity

    def enqueue(self, item):
        """method that adds an item to the queue
        Args:
            item (any type): item that is to be added to queue
        Returns:
            None
        """
        if self.is_full():
            raise IndexError
        temp = Node(item)
        self.num_items += 1
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        """method that removes the item in front of the queue
        Args:
            No args
        Returns:
            Data (any type): the data that was first in queue
        """
        if self.is_empty():
            raise IndexError
        val = self.front
        self.front = val.next
        self.num_items -= 1
        if self.front is None:
            self.rear = None
        return val.val

    def size(self):
        """method that gives number of items in stack
        Args:
            No args
        Returns:
            int: the number of items stored in the queue
        """
        return self.num_items
