#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch8_Ex3.py
    Author:             Matt Randazzo
    Date created:       3/9/2019
    Date last modified: 3/9/2019
    Python Version:     3.7

    Description: CTCI 8.3 Magic Index
                 A magic index in an array A[0... n-1] is defined to be an index such that A[i] = i.
                 Given a sorted array of distinct integers, write a method to find a magic index, if
                 one exists, in array A.

    Classes:

            find_magic_number_brute_force
            find_magic_number_distinct
            find_magic_number_non_distinct

    Functions:

"""


def find_magic_number_brute_force(numbers):
    """Find magic number using brute force O(n)

    :param numbers array of sorted unique integers
    :param magic   magic number to be searched for
    :return        index of magic number, else -1

    """
    for index in range(len(numbers)):
        if numbers[index] == index:
            return index
    return -1


def find_magic_number_distinct(numbers):
    """Find magic number in list of distinct numbers

    :param numbers List of sorted distinct integers
    :return        Index of magic number or -1

    """

    def magic_number_helper(numbers, min_num, max_num):
        """Find magic number in list of distinct numbers

        :param numbers List of sorted distinct integers
        :param min_num minimum index
        :param max_num maximum index
        :return        Index of magic number or -1

        """
        if min_num > max_num:
            return -1
        middle = (max_num + min_num) // 2

        if numbers[middle] == middle:
            return middle
        elif numbers[middle] > middle:
            return magic_number_helper(numbers, min_num, middle - 1)
        elif numbers[middle] < middle:
            return magic_number_helper(numbers, middle + 1, max_num)

    return magic_number_helper(numbers, 0, len(numbers) - 1)


def find_magic_number_non_distinct(numbers):
    """Find magic number in list of non-distinct numbers

    :param numbers List of sorted distinct integers
    :return        Index of magic number or -1

    """
    def magic_number_helper(numbers, min_num, max_num):
        """Find magic number in list of non- distinct numbers

        :param numbers List of sorted distinct integers
        :param min_num minimum index
        :param max_num maximum index
        :return        Index of magic number or -1

        """
        if min_num > max_num:
            return -1
        middle = (max_num + min_num) // 2

        if numbers[middle] == middle:
            return middle

        left_index = min(numbers[middle], middle - 1)
        left = magic_number_helper(numbers, min_num, left_index)
        if left >= 0:
            return left

        right_index = max(numbers[middle], middle + 1)
        right = magic_number_helper(numbers, right_index, max_num)
        if right >= 0:
            return right
        return -1

    return magic_number_helper(numbers, 0, len(numbers) - 1)
