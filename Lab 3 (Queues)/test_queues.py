import unittest
from linked_list import Node
from queues import QueueArray
from queues import QueueLinked


class TestCase(unittest.TestCase):
    def test_enqueue(self):
        queue_l = QueueLinked(0)
        self.assertRaises(IndexError, queue_l.enqueue, 10)
        queue_l = QueueLinked(1)
        queue_l.enqueue(10)
        self.assertEqual(queue_l.rear, Node(10))
        queue_a = QueueArray(1)
        queue_a.enqueue(7)
        self.assertEqual(queue_a.items, [7, None])
        self.assertRaises(IndexError, queue_a.enqueue, 20)

    def test_size(self):
        queue_a = QueueArray(2)
        queue_l = QueueLinked(2)
        self.assertEqual(queue_a.size(), 0)
        self.assertEqual(queue_l.size(), 0)
        queue_a.num_items = 20
        queue_l.num_items += 1
        self.assertEqual(queue_a.size(), 20)
        self.assertEqual(queue_l.size(), 1)

    def test_is_full(self):
        queue_a = QueueArray(1)
        queue_l = QueueLinked(2)
        self.assertFalse(queue_a.is_full())
        self.assertFalse(queue_l.is_full())
        queue_a.num_items = 1
        queue_l.num_items += 2
        queue_a.rear += 1
        self.assertTrue(queue_a.is_full())
        self.assertTrue(queue_l.is_full())

    def test_is_empty(self):
        queue_a = QueueArray(1)
        queue_l = QueueLinked(2)
        self.assertTrue(queue_a.is_empty())
        self.assertTrue(queue_l.is_empty())
        queue_a.num_items = 1
        queue_l.num_items += 2
        self.assertFalse(queue_a.is_empty())
        self.assertFalse(queue_l.is_empty())

    def test_dequeue(self):
        queue_l = QueueLinked(1)
        queue_l.rear, queue_l.front, queue_l.num_items = Node(10), Node(10), 1
        self.assertEqual(queue_l.dequeue(), 10)
        self.assertRaises(IndexError, queue_l.dequeue)
        queue_a = QueueArray(1)
        queue_a.front, queue_a.rear, queue_a.num_items = 0, 1, 1
        queue_a.items = [10, None]
        self.assertEqual(queue_a.dequeue(), 10)
        self.assertRaises(IndexError, queue_a.dequeue)


def main():
    unittest.main()


if __name__ == '__main__':
    main()