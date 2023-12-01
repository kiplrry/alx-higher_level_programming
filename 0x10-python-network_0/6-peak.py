#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    length = len(list_of_integers)
    cent = length
    mid = length // 2

    if length == 0:
        return None

    while True:
        cent = cent // 2
        if (mid < length - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if cent // 2 == 0:
                cent = 2
            mid = mid + cent // 2
        elif cent > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if cent // 2 == 0:
                cent = 2
            mid = mid - cent // 2
        else:
            return list_of_integers[mid]
