"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
	def pair(f):
		return f(a,b)
	return pair

def car(pair):
	def first_element(a,b):
		return a
	return pair(first_element)

def cdr(pair):
	def last_element(a,b):
		return b
	return pair(last_element)

if __name__ == "__main__":
	foo = car(cons(3,4))
	bar = cdr(cons(3,4))

	print(f"car(cons(3,4) = {foo}")
	print(f"cdr(cons(3,4) = {bar}")