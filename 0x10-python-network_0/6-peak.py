#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ Use loop instead of recursion to find the peak"""
    someList = list_of_integers
    if len(someList) == 0:
        return None
    left, right = 0, len(someList) - 1
    while left < right:
        mid = (left + right) // 2
        if someList[mid] < someList[mid+1]:
            left = mid + 1
        else:
            right = mid
    return someList[left]
