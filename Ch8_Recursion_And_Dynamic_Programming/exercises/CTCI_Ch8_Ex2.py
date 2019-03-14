#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch8_Ex2.py
    Author:             Matt Randazzo
    Date created:       3/5/2019
    Date last modified: 3/13/2019
    Python Version:     3.7

    Description: CTCI 8.2 Robot in a Grid
                 Imagine a robot sitting on the upper left corner of a grid with r rows
                 and c columns. The robot can only move in two directions, right and down,
                 but certain cells are "off limits" such that the robot cannot step on them.
                 Design an algorithm to find a path for the robot from the top left to the
                 bottom right.
    Classes:

    Functions:

            to_bottom_right      find path to origin from top left
            to_bottom_right_memo memoized find path to origin from top left

"""


def to_bottom_right(grid_size=3, off_limits=()):
    """Return path to bottom right of grid

    :param grid_size Height and width of the grid
    :return          Path to origin

    """

    def to_bottom_right_helper(m, n, moves):
        """Helper function to return path to bottom right of grid

        :param m     x position
        :param n     y position
        :param moves path taken (Ex. right, down, right)

        """
        if (m, n) in off_limits:
            return False
        elif m < 0 or n < 0:
            return False
        elif (m, n) == (0, 0) or to_bottom_right_helper(m-1, n, moves + ["right"]) or \
                   to_bottom_right_helper(m, n-1, moves + ["down"]):
            return True
        else:
            return False

    return to_bottom_right_helper(grid_size, grid_size, [])


def to_bottom_right_memo(grid_size=3, off_limits=()):
    """Memoized path to bottom right of grid

    :param grid_size Height and width of the grid
    :return          Path to origin

    """

    def to_bottom_right_helper(m, n, moves):
        """Helper function to return path to bottom right of grid

        :param m      x position
        :param n      y position
        :param moves  path taken (Ex. right, down, right)
        :param failed failed points

        """
        if (m, n) in off_limits:
            return False
        elif m < 0 or n < 0:
            return False
        elif (m, n) in failed:
            return False
        elif (m, n) == (0, 0) or to_bottom_right_helper(m-1, n, moves + ["right"]) or \
                to_bottom_right_helper(m, n-1, moves + ["down"]):
            return True
        else:
            failed.append((m, n))
            return False
    failed = []

    return to_bottom_right_helper(grid_size, grid_size, [])
