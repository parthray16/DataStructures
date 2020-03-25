"""LAB1
CPE202
"""

#1
def get_max(ints):
    """find the max integer of a given list of integers
    Args:
        ints (list): a list of integers
    Return:
        int : max integer in ints
    """
    if len(ints) == 0:
        return None
    max_int = ints[0]
    for i in ints:
        if i > max_int:
            max_int = i
    return max_int

#2
def reverse(string):
    """reverse the given string
    Args:
        string (str) : a string
    Return:
        str : reversed string
    """
    if len(string) == 0:
        return ""
    return reverse(string[1:]) + string[0]

#3
def search(ints, target):
    """search for value (target) in sorted list of integers (ints)
    Args:
        ints (list) : list of sorted integers
        target (int) : target value to search for
    Return:
        int : index of target in ints (list)
        None : if integer not in the list
    """
    return binary_search(ints, target, 0, len(ints) - 1)


def binary_search(ints, target, start, end):
    """binary search for value (target) in sorted list of integers (ints)
    Args:
        ints (list) : list of sorted integers
        target (int) : target value to search for
        start (int) : the index of where to start searching for target
        end (int) : the index of where to end searching for target
    Return:
        int : index of target in ints (list)
        None : if integer not in the list
    """
    if start > end:
        return None
    middle = (start + end) // 2
    if target == ints[middle]:
        return middle
    if target > ints[middle]:
        return binary_search(ints, target, middle + 1, end)
    return binary_search(ints, target, start, middle - 1)

#4
def fib(target):
    """recursively compute the nth (target) Fibonacci number of Fibonacci Numbers
    Args:
        target (int) : integer value greater than or equal to 0
    Return:
        int : the nth (target) Fibonacci number
    """
    if target == 0:
        return 0
    if target == 1:
        return 1
    return fib(target - 1) + fib(target - 2)

#5.1 factorial iterative version
def factorial_iter(target):
    """iteratively compute the factorial of target
    Args:
        target (int) : integer value greater than or equal to zero
    Return:
        int : the factorial of target value
    """
    fac = 1
    while target > 0:
        fac *= target
        target -= 1
    return fac

#5.2 factorial recursive version
def factorial_rec(target):
    """recursively compute the factorial of target
    Args:
        target (int) : integer value greater than or equal to zero
    Return:
        int : the factorial of target
    """
    if target in (0, 1):
        return 1
    return target * factorial_rec(target - 1)
