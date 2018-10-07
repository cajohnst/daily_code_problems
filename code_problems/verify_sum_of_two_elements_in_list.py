"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import time
import random

def verify_sum(foo:list, k:float) -> bool:
	# non-modified list
	for i in foo:
		for j in foo:
			if i <= j:
				continue
			else:
				if i + j == k:
					return i, j, k, True
	return False

def verify_sum_with_modified_list(foo:list, k:float) -> bool:
	# attempt to copy and modify original list through iterations

	for ix, i in enumerate(foo):
		if not ix == len(foo):
			mod_foo = foo[ix+1:]
			for j in mod_foo:
				if i + j == k:
					return i, j, k, True
	return False

if __name__ == "__main__":
	k = random.randint(1, 25)

	foo = random.sample(range(1, 25), 10)

	start_time_1 = time.time()
	result1 = verify_sum(foo, k)

	process_time_1 = time.time() - start_time_1

	start_time_2 = time.time()
	result2 = verify_sum_with_modified_list(foo, k)

	process_time_2 = time.time() - start_time_2

	print(f"result 1: {result1} \n result2: {result2}")
	print(f"verify_sum process time: {process_time_1} \n verify_sum_modified process time: {process_time_2}")

