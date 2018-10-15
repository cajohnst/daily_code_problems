"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

from collections import defaultdict 

class TrieNode(object):
	def __init__(self, char=None):
		self.char = char 
		self.children = defaultdict(TrieNode)
		self.end_of_word = False 

def add_node(root, word):
	cur_node = root 
	for char in word:
		if char in cur_node.children:
			cur_node = cur_node.children[char]
		else:
			new_node = TrieNode(char)
			cur_node.children[char] = new_node
			cur_node = new_node
	
	cur_node.end_of_word = True

def search(root, auto_complete_str):
	"""
	params:
		root(TrieNode): the root of tree
		auto_complete_str: query string for auto-complete
	return:
		list: list of all possible results
	"""

	cur_node = root
	result = []

	for char in auto_complete_str:
		if char in cur_node.children: 	# if able to auto-complete
			cur_node = cur_node.children[char]
			result.append(char)
		else: # no matches
			return [] # return blank list 

	


