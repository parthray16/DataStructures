"""Lab 6
   Parth Ray
"""
import random

def selection_sort(alist):
    """Author: Parth Ray
    sorts list of integers to ascending order using selection sort
    Args:
        alist (list): a list of integers
    Returns:
        int: number of comparisons made
    """
    comparisons = 0
    for i in range(len(alist)):
        min_val = alist[i]
        index = i
        for j in range(i + 1, len(alist)):
            comparisons += 1
            if alist[j] < min_val:
                min_val = alist[j]
                index = j
        alist[i], alist[index] = min_val, alist[i]
    return comparisons


def quick_sort(alist, low=0, high=None, comparisons=0):
    """Author: Parth Ray
    recursively sorts list of integers to ascending order using quick sort
    Args:
        alist (list): a list of integers
        low (int): pointer to first index, default 0
        high (int): pointer to last index, default None
        comparisons (int): number of comparisons, default 0
    Returns:
        int: number of comparisons made
    """
    if high is None:
        high = len(alist) - 1
    if low >= high:
        return None
    mid = (low + high) // 2
    alist[low], alist[mid] = alist[mid], alist[low]
    left = low + 1
    right = high
    while left <= right:
        comparisons += 1
        while left <= high and alist[left] <= alist[low]:
            left += 1
        while right > low and alist[low] <= alist[right]:
            right -= 1
        if left <= right:
            alist[left], alist[right] = alist[right], alist[left]
    alist[low], alist[right] = alist[right], alist[low]
    quick_sort(alist, low, right - 1, comparisons)
    quick_sort(alist, right + 1, high, comparisons)
    return comparisons
