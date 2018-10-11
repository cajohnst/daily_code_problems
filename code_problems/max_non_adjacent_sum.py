"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

import random

def find_largest_sum_of_non_adjacent_ints(arr):
    """
    Find the largest sum of integers that are not adjacent in a list object

    dtype arr: list
    rtype: int
    """

    # define place holder vars in memory
    res, prev1, prev2 = 0, 0, 0

    for ix, val in enumerate(arr):
        if ix == 0:
            res = val
        elif ix == 1:
            res = max(prev1, val)
        else:
            res = max(prev1, val + prev2)

        prev2 = prev1
        prev1 = res 

    return res 

if __name__ == "__main__":
    foo = random.sample(range(-25, 25), 7)

    max_sum = find_largest_sum_of_non_adjacent_ints(foo)


