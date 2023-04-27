#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ Use algorithm to find the peak"""
    someList = list_of_integers
    n = len(someList)
    if n == 1:
        return someList[0]
    elif n == 2:
        return max(someList)
    else:
        mid_index = n // 2
        if someList[mid_index] < someList[mid_index-1]:
            return find_peak(someList[:mid_index])  # from the first to mid
        elif someList[mid_index] < someList[mid_index+1]:
            return find_peak[someList[mid_index+1:]]  # from mid to the last
        else:
            return someList[mid_index]
