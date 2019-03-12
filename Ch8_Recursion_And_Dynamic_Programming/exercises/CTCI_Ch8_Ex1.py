#!/usr/bin/env python
"""
    File name:          test_CTCI_Ch8_Ex1.py
    Author:             Matt Randazzo
    Date created:       3/3/2019
    Date last modified: 3/11/2019
    Python Version:     3.7

    Description: CTCI 8.1 Triple Step
                 A child is running up a staircase with n steps and can hop either 1 step
                 2 steps, or 3 steps at a time. Implement a method to count how many
                 possible ways the child can run up the stairs.
    Classes:

            None

    Functions:

            memoization             dynamic programming wrapper function
            triple_step_combination Recursive solution to three step problem
            memoized_triple_step    three step problem with memoization wrapper

"""


def memoization(func):
    """Memoize the triple_step_combination

    :param func function to be wrapped in memoization dictionary

    """
    memo = {}

    def wrapper(arg):
        """Inner memoization wrapper function

        :param arg arguments used in input function

        """
        if arg not in memo:
            memo[arg] = func(arg)
        return memo[arg]
    return wrapper


def triple_step_combinations(step):
    """Find number of step combinations for maximum of three steps at a time

    :param step Number of steps left
    :return     Number of step combinations

    """
    if step < 0:
        return 0
    elif step == 0:
        return 1
    return triple_step_combinations(step - 3) + \
        triple_step_combinations(step - 2) + \
        triple_step_combinations(step - 1)


@memoization
def memoized_triple_step(step):
    """Find number of step combinations for maximum of three steps at a time

    :param step Number of steps left
    :return     Number of step combinations

    """
    if step < 0:
        return 0
    elif step == 0:
        return 1
    return memoized_triple_step(step - 3) + \
        memoized_triple_step(step - 2) + \
        memoized_triple_step(step - 1)
