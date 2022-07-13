"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Hints: #44, #177, #132
"""


# solution 1 - hash table
def isUnique1(text):
	"""
	O(n)
	n - len(trail_text)
	use hash table
	:param text:
	"""
	
	visited_char = {}
	for char in text:
		if char in visited_char.keys():
			return False
		visited_char[char] = 1
	return True


# solution 2 - official solution - use ASCII index or unicode index
def isUnique2(text):
	"""
	time: O(n)
	space: O(1)
	
	:param text: string
	:return: bool
	"""
	# length of text exceed the number of ascii chars (total 128 chars)
	if len(text) > 128:
		return False
	
	# init a list of 128 False which is the same number of ASCII chars
	# use letter of text as index, check status[letter] is false:
	# yes -> change to True, No -> found a duplicate char
	status = [False] * 128
	for letter in text:
		if status[ord(letter)]:
			return False
		status[ord(letter)] = True
	return True

	
if __name__ == '__main__':
	inputs = ['what is', 'what is it']
	for text in inputs:
		res = isUnique1(text)
		print(f"'{text}' is {res}")

