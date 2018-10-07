"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
import time
import random 

def product_array_excluding_ith_element(foo:list) -> list:
	# create new list bar
	bar = []

	for i in foo:
		k = 1 
		for j in foo:
			if i == j:
				continue 
			else:
				k = k * j
		bar.append(k)

	return bar 


if __name__ == "__main__":
	foo = random.sample(range(1, 5), 4)

	start_time = time.time()

	bar = product_array_excluding_ith_element(foo)

	process_time = time.time() - start_time

	print(f"foo: {foo} \n bar: {bar}")
	print(f"Function process time: {process_time} seconds.")

