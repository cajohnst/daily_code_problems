"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
import random 
import string

def count_longest_substr(k, string):
	"""
	params:
		k: int representing the number of distinct characters in substring
		string: str the string of which to query

	return:
		int representing the length of the longest substring
	"""
	max_char_count = 0

	for start_ix in range(len(string)):
		end_sub_ix = start_ix + k 

		if end_sub_ix <= len(string) - 1:
			# the first index ought to be at least k values from the starting index
			for end_ix in range(end_sub_ix, len(string)):
				dist_char_count = len(set(string[start_ix:end_ix]))

				if dist_char_count > k:
					break 
				else:
					len_sub = end_ix - start_ix 
					max_char_count = max(max_char_count, len_sub)

	return max_char_count 

if __name__ == "__main__":
	rand_str = "".join(random.choice(["a", "b", "c", "d"]) for i in range(10))

	print(rand_str)
	max_distinct_chars = count_longest_substr(3, rand_str)

	print(max_distinct_chars)



