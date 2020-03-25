import unittest
from lab1 import get_max
from lab1 import reverse
from lab1 import search
from lab1 import fib
from lab1 import factorial_iter
from lab1 import factorial_rec

class TestCase(unittest.TestCase):


    def test_get_max(self):
        arr = [1,2,3,4,5]
        self.assertEqual(get_max(arr), 5)
        arr = [30, 29, 20, 10, 5, 2]
        self.assertEqual(get_max(arr), 30)
        arr = []
        self.assertEqual(get_max(arr), None)


    def test_reverse(self):
        self.assertEqual(reverse("qweEerty"), "ytreEewq")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("tacocat"), "tacocat")
        self.assertEqual(reverse("GUARANTEE"), "EETNARAUG")
        self.assertEqual(reverse("Parth"), "htraP")


    def test_search(self):
        arr = [1,2,3,4,5]
        self.assertEqual(search(arr, 5), 4)
        arr = []
        self.assertEqual(search(arr, 5), None)
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(search(arr, 6), 5)
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(search(arr, 17), None)
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(search(arr, 2), 1)


    def test_fib(self):
        def fib_numbers(n):
            sequence = []
            for i in range(n+1):
                sequence.append(fib(i))
            return sequence

        #this will test your fib function by calling it multiple times
        self.assertEqual(fib_numbers(10),
                [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_factorial(self):
        self.assertEqual(factorial_iter(3), 6)
        self.assertEqual(factorial_iter(0), 1)
        self.assertEqual(factorial_iter(1), 1)
        self.assertEqual(factorial_iter(5), 120)
        self.assertEqual(factorial_iter(3), factorial_rec(3))
        self.assertEqual(factorial_rec(0), 1)
        self.assertEqual(factorial_rec(5), 120)


def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()
