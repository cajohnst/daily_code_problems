"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

import random 
import time

def find_first_missing_pos_int(int_array:list, use_built_in_max=False) -> int:
    # first find the largest int in the array
    # could use max function or create own implementation
    if use_built_in_max is False:
        max_int = find_max_int_in_list(int_array)
    elif use_built_in_max is True:
        max_int = max(int_array)

    if max_int > 0:
        positive_int_array = create_positive_array_list(max_int)

        for i in positive_int_array:
            if not i in int_array:
                return i
    
    else:
        return None

def find_max_int_in_list(int_array:list) -> int:
    max_val = None 

    for i in int_array:
        if max_val is None:
            max_val = i 
        elif i > max_val:
            max_val = i 

    return max_val

def create_positive_array_list(max_val:int) -> list:
    # create a list of positive int vals from 1 to the largest int in original array
    # add 1 to list in case all ints in list are sequential

    positive_int_array = range(1, max_val + 1, 1)

    return positive_int_array


if __name__ == "__main__":
    foo = random.sample(range(-25, 25), 10)

    start_time = time.time()
    lowest_int = find_first_missing_pos_int(foo, use_built_in_max=False)

    process_time = time.time() - start_time

    start_2 = time.time()
    lowest_int = find_first_missing_pos_int(foo, use_built_in_max=True)

    process_2 = time.time() - start_2

    print(foo)
    print(lowest_int)
    print(f"Completed processing w/out built-in max in {process_time} seconds.")
    print(f"Completed processing w/ built-in max in {process_2} seconds.")



