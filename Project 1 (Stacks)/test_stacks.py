import unittest
import stacks
from stacks import StackArray
from stacks import StackLinked

class TestCase(unittest.TestCase):
    def test_push(self):
        stack_1a = StackArray()
        stack_1a.push(7)
        stack_2a = StackArray()
        stack_2a.arr_list.arr = [7, None]
        stack_2a.arr_list.num_items = 1
        stack_2a.num_items = 1
        self.assertEqual(stack_1a, stack_2a)
        stack_1l = StackLinked()
        stack_1l.push(7)
        stack_2l = StackLinked()
        stack_2l.top = stacks.Node(7, None)
        stack_2l.num_items = 1
        self.assertEqual(stack_1l, stack_2l)

    def test_is_empty(self):
        stacka = StackArray()
        self.assertTrue(stacka.is_empty())
        stacka.num_items += 1
        self.assertFalse(stacka.is_empty())
        stackl = StackLinked()
        self.assertTrue(stackl.is_empty())
        stackl.num_items += 1
        self.assertFalse(stackl.is_empty())


    def test_pop(self):
        stacka = StackArray()
        self.assertRaises(IndexError, stacka.pop)
        stacka.num_items = 2
        stacka.arr_list.arr = [1, 2]
        stacka.arr_list.num_items = 2
        self.assertEqual(stacka.pop(), 2)
        stackl = StackLinked()
        self.assertRaises(IndexError, stackl.pop)
        stackl.top = stacks.Node(1, None)
        stackl.num_items = 1
        self.assertEqual(stackl.pop(), 1)


    def test_peek(self):
        stacka = StackArray()
        self.assertRaises(IndexError, stacka.peek)
        stacka.num_items = 2
        stacka.arr_list.arr = [1, 2]
        stacka.arr_list.num_items = 2
        self.assertEqual(stacka.peek(), 2)
        stackl = StackLinked()
        self.assertRaises(IndexError, stackl.peek)
        stackl.top = stacks.Node(1, None)
        stackl.num_items = 1
        self.assertEqual(stackl.peek(), 1)

    def test_size(self):
        stacka = StackArray()
        self.assertEqual(stacka.size(), 0)
        stackl = StackLinked()
        stackl.num_items = 20
        self.assertEqual(stackl.size(), 20)

def main():
    unittest.main()


if __name__ == '__main__':
    main()