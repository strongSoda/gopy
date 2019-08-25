"""Linear Search Implementation
Takes in an item & array & returns the index of match
"""

def search(item,array):
	for i in range(len(list(array))):
		if array[i] == item:
			return i
	return "Not Found"