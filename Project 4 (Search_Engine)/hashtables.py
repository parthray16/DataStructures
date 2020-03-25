"""Lab 8
Parth Ray
"""
from linked_list import Node

class Pair:
    """class that maps a key value pair
    Attributes:
        key (*): any item
        data (*): any data
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.data = value

    def __eq__(self, other):
        return isinstance(other, Pair) \
                and self.key == other.key \
                and self.data == other.data

    def __repr__(self):
        return f"{{{self.key}: {self.data}}}"

    def __getitem__(self, idx):
        if idx == 0:
            return self.key
        if idx == 1:
            return self.data
        raise IndexError


class Dummy:
    """Dummy object used as a special marker
    """
    def __init__(self):
        pass


class HashTableSepchain:
    """creates a hash table that stores key-item pairs using Separate Chaining
    Attributes:
        table_size (int): size of hash table, default=11
        table (list): the hash table
        num_items (int): number of key-item pairs in table
        num_collisions (int): number of collisions while inserting
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.table = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0

    def __eq__(self, other):
        return isinstance(other, HashTableSepchain) \
                and self.table_size == other.table_size \
                and self.table == other.table \
                and self.num_items == other.num_items \
                and self.num_collisions == other.num_collisions

    def __repr__(self):
        return f"HashTable({self.table})"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """this method inserts key-item pair into the hash table
        Args:
            key (str): a string key
            data (*): any item
        """
        if self.load_factor() >= 1.5:
            self.resize()
        idx = hash_string(key, self.table_size)
        item = self.table[idx]
        if item is None:
            self.table[idx] = Node(Pair(key, data))
            self.num_items += 1
        else:
            while item:
                if item.val.key == key:
                    item.val.data = data
                    return
                item = item.next
            self.num_collisions += 1
            node = self.table[idx]
            self.table[idx] = Node(Pair(key, data), node)
            self.num_items += 1

    def get(self, key):
        """this method gets key-item pair from the hash table given a key
        Args:
            key (str): a string key
        Returns:
            str : the key that was removed
            * : the data associated with the key that was removed
        Raises:
            KeyError: if key not in the table
        """
        idx = hash_string(key, self.table_size)
        item = self.table[idx]
        while item:
            if item.val.key == key:
                return item.val.data
            item = item.next
        raise KeyError

    def contains(self, key):
        """this method returns True if the key exists in the table, otherwise returns False
        Args:
            key (str): a string key
        Returns:
            Boolean: True if key exists in table, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """this method removes key-item pair from the hash table and returns pair removed
        Args:
            key (str): a string key
        Returns:
            str : the key that was removed
            * : the data associated with the key that was removed
        Raises:
            KeyError: if key not in the table
        """
        idx = hash_string(key, self.table_size)
        item = self.table[idx]
        prev = None
        while item:
            if item.val.key == key:
                self.num_items -= 1
                if prev:
                    prev.next = item.next
                    return item.val.key, item.val.data
                self.table[idx] = item.next
                return item.val.key, item.val.data
            prev = item
            item = item.next
        raise KeyError

    def resize(self):
        """this method increases the number of slots in the hash table to twice the old number
           of slots, plus 1 (new_size = 2*old_size + 1). After creating the new hash table,
           the items in the old hash table are rehashed into the new table
        """
        num_items, num_collisions = self.num_items, self.num_collisions
        old_table = self.table
        self.table_size = (2 * self.table_size) + 1
        self.table = [None] * self.table_size
        for item in old_table:
            if item:
                node = item
                while node:
                    self.put(node.val.key, node.val.data)
                    node = node.next
        self.num_items, self.num_collisions = num_items, num_collisions

    def size(self):
        """this method returns number of key-item pairs in hash table
        Returns:
            int: number of items in hash table
        """
        return self.num_items

    def load_factor(self):
        """this method returns load factor of hash table
        Returns:
            float: load factor of hash table
        """
        return self.size() / self.table_size

    def collisions(self):
        """this method returns number of collisions during insertion in hash table
        Returns:
            int: number of collisions in hash table
        """
        return self.num_collisions


class HashTableLinear:
    """creates a hash table that stores key-item pairs using Linear Probing
    Attributes:
        table_size (int): size of hash table, default=11
        table (list): the hash table
        num_items (int): number of key-item pairs in table
        num_collisions (int): number of collisions while inserting
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.table = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0

    def __eq__(self, other):
        return isinstance(other, HashTableLinear) \
                and self.table_size == other.table_size \
                and self.table == other.table \
                and self.num_items == other.num_items \
                and self.num_collisions == other.num_collisions

    def __repr__(self):
        return f"HashTable({self.table})"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """this method inserts key-item pair into the hash table
        Args:
            key (str): a string key
            data (*): any item
        """
        if self.load_factor() >= .75:
            self.resize()
        idx = hash_string(key, self.table_size)
        slot = self.table[idx]
        if slot is None:
            self.table[idx] = Pair(key, data)
            self.num_items += 1
        else:
            if slot.key == key:
                slot.data = data
            else:
                idx = rehash(idx, self.table_size)
                while self.table[idx]:
                    if self.table[idx].key == key:
                        self.table[idx] = Pair(key, data)
                        return
                    idx = rehash(idx, self.table_size)
                self.num_collisions += 1
                self.table[idx] = Pair(key, data)
                self.num_items += 1

    def get(self, key):
        """this method gets key-item pair from the hash table given a key
        Args:
            key (str): a string key
        Returns:
            str : the key that was removed
            * : the data associated with the key that was removed
        Raises:
            KeyError: if key not in the table
        """
        idx = hash_string(key, self.table_size)
        while self.table[idx]:
            if self.table[idx].key == key:
                return self.table[idx].data
            idx = rehash(idx, self.table_size)
        raise KeyError


    def contains(self, key):
        """this method returns True if the key exists in the table, otherwise returns False
        Args:
            key (str): a string key
        Returns:
            Boolean: True if key exists in table, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """this method removes key-item pair from the hash table and returns pair removed
        Args:
            key (str): a string key
        Returns:
            str : the key that was removed
            * : the data associated with the key that was removed
        Raises:
            KeyError: if key not in the table
        """
        if key not in self:
            raise KeyError
        idx = hash_string(key, self.table_size)
        while key != self.table[idx].key:
            idx = rehash(idx, self.table_size)
        temp = self.table[idx]
        self.table[idx] = None
        idx = rehash(idx, self.table_size)
        while self.table[idx]:
            redo = self.table[idx]
            self.table[idx] = None
            self.put(redo.key, redo.data)
            idx = rehash(idx, self.table_size)
        return temp.key, temp.data


    def resize(self):
        """this method increases the number of slots in the hash table to twice the old number
           of slots, plus 1 (new_size = 2*old_size + 1). After creating the new hash table,
           the items in the old hash table are rehashed into the new table
        """
        num_items, num_collisions = self.num_items, self.num_collisions
        old_table = self.table
        self.table_size = (2 * self.table_size) + 1
        self.table = [None] * self.table_size
        for item in old_table:
            if item:
                self.put(item.key, item.data)
        self.num_items, self.num_collisions = num_items, num_collisions

    def size(self):
        """this method returns number of key-item pairs in hash table
        Returns:
            int: number of items in hash table
        """
        return self.num_items

    def load_factor(self):
        """this method returns load factor of hash table
        Returns:
            float: load factor of hash table
        """
        return self.size() / self.table_size

    def collisions(self):
        """this method returns number of collisions during insertion in hash table
        Returns:
            int: number of collisions in hash table
        """
        return self.num_collisions


class HashTableQuadratic:
    """creates a hash table that stores key-item pairs using Quadratic Probing
    Attributes:
        table_size (int): size of hash table, default=11
        table (list): the hash table
        num_items (int): number of key-item pairs in table
        num_collisions (int): number of collisions while inserting
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.table = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0

    def __eq__(self, other):
        return isinstance(other, HashTableQuadratic) \
                and self.table_size == other.table_size \
                and self.table == other.table \
                and self.num_items == other.num_items \
                and self.num_collisions == other.num_collisions

    def __repr__(self):
        return f"HashTable({self.table})"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """this method inserts key-item pair into the hash table
        Args:
            key (str): a string key
            data (*): any item
        """
        if self.load_factor() >= .75:
            self.resize()
        idx = hash_string(key, self.table_size)
        slot = self.table[idx]
        if slot is None or slot is Dummy:
            self.table[idx] = Pair(key, data)
            self.num_items += 1
        else:
            if slot.key == key:
                slot.data = data
            else:
                i = 1
                idx = (idx + (i * i)) % self.table_size
                while self.table[idx]:
                    if self.table[idx] is Dummy:
                        self.table[idx] = Pair(key, data)
                        self.num_items += 1
                        return
                    if self.table[idx].key == key:
                        self.table[idx] = Pair(key, data)
                        return
                    i += 1
                    idx = (idx + (i * i)) % self.table_size
                self.num_collisions += 1
                self.table[idx] = Pair(key, data)
                self.num_items += 1

    def get(self, key):
        """this method gets key-item pair from the hash table given a key
        Args:
            key (str): a string key
        Returns:
            str : the key that was removed
            * : the data associated with the key that was removed
        Raises:
            KeyError: if key not in the table
        """
        idx = hash_string(key, self.table_size)
        i = 1
        while self.table[idx]:
            if (isinstance(self.table[idx], Dummy)) or self.table[idx].key != key:
                idx = idx + (i * i) % self.table_size
                i += 1
            else:
                break
        if self.table[idx] is None:
            raise KeyError
        return self.table[idx].data

    def contains(self, key):
        """this method returns True if the key exists in the table, otherwise returns False
        Args:
            key (str): a string key
        Returns:
            Boolean: True if key exists in table, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """this method removes key-item pair from the hash table and returns pair removed
        Args:
            key (str): a string key
        Raises:
            KeyError: if key not in the table
        """
        idx = hash_string(key, self.table_size)
        i = 1
        while self.table[idx]:
            if (isinstance(self.table[idx], Dummy)) or self.table[idx].key != key:
                idx = idx + (i * i) % self.table_size
                i += 1
            else:
                break
        if self.table[idx] is None:
            raise KeyError
        self.table[idx] = Dummy()


    def resize(self):
        """this method increases the number of slots in the hash table to twice the old number
           of slots, plus 1 (new_size = 2*old_size + 1). After creating the new hash table,
           the items in the old hash table are rehashed into the new table
        """
        num_items, num_collisions = self.num_items, self.num_collisions
        old_table = self.table
        self.table_size = (2 * self.table_size) + 1
        self.table = [None] * self.table_size
        for item in old_table:
            if item:
                self.put(item.key, item.data)
        self.num_items, self.num_collisions = num_items, num_collisions

    def size(self):
        """this method returns number of key-item pairs in hash table
        Returns:
            int: number of items in hash table
        """
        return self.num_items

    def load_factor(self):
        """this method returns load factor of hash table
        Returns:
            float: load factor of hash table
        """
        return self.size() / self.table_size

    def collisions(self):
        """this method returns number of collisions during insertion in hash table
        Returns:
            int: number of collisions in hash table
        """
        return self.num_collisions


def hash_string(string, size):
    """generates a hash value for a string
    Args:
        string (str): the string you want to hash
        size (int): table_size of the hash table
    Returns:
        int: the hash of the string
    """
    hash_idx = 0
    for char in string:
        hash_idx = (hash_idx * 31 + ord(char)) % size
    return hash_idx


def rehash(hash_idx, size):
    """rehashes hash depending on type of hash table
    Args:
        hash_idx (int): hash value
        size (int): table_size of hash table
        probe (string): type of hash table
    Returns:
        int: rehashed value
    """
    return (hash_idx + 1) % size

def import_stopwords(filename, hashtable):
    """puts words from file into a hash table
    Args:
        filename (str): the string name of a text file
        hashtable (HashTable): a HashTable object
    Returns:
        HashTable: the Hashtable object containing the words from the text file
    """
    file = open(filename, "r")
    stopwords = (file.readline()).split()
    for i in stopwords:
        hashtable.put(i, i)
    file.close()
    return hashtable

def keys(hashtable):
    """extract all key value pairs stored in the hash table.
       Files with scores being 0 will be ignored
    Args:
        hashtable (HashTable): a HashTable object
    Returns:
        list : list of Pairs
    """
    return [i for i in hashtable.table if i.data != 0]
