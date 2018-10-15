"""
This problem was asked by Google.
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values
of the array so that all the Rs come first, the Gs come second, and the Bs come
last. You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
import time
import random

class RGBarray(object):
	def __init__(self, array):
		self.array = array

	def sort_list_in_place(self):
		"""
		params
			array:list 
		return
			list 

		This function will accept an input array and 
		sort by the letters according to the preference
		"R", "G", "B"

		""" 
		num_el = len(self.array)

		for i in range(num_el):
			if i != num_el - 1:			
				if (self.array[i+1] == "R") & (self.array[i] != "R"): 	# if next element is R and current element is not R, swap
					self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
				
				if (self.array[i] == "B") & (self.array[i+1] != "B"): 	# if current element is B and next element is not B, swap
					self.array[i+1], self.array[i] = self.array[i], self.array[i+1]

if __name__ == "__main__":
	rgb_arr = [random.choice("RGB") for _ in range(7)]
	rgb_arr_cp = rgb_arr 

	print(rgb_arr)

	"""
	Note ***
		Current method is about twice as slow as the built in sort method 
	"""
	
	start_built_in_method_time = time.time()
	rgb_arr.sort(reverse=True)
	process_built_in_method_time = time.time() - start_built_in_method_time

	print(rgb_arr)
	print(process_built_in_method_time)

	rgb_array = RGBarray(rgb_arr_cp)
	start_custom_sort_time = time.time()
	rgb_array.sort_list_in_place()
	process_custom_sort_time = time.time() - start_custom_sort_time

	print(process_custom_sort_time)










