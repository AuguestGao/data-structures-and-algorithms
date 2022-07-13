"""
Given two strings, check if they are anagrams, i.e. same letter with different arrangement.
example:
"public relations" is an anagram of "crap built on lies"

ignore spaces and capitals
"""


# solution 1 - O(n)
def isAnagram1(a, b):
	a = a.replace(' ', '').lower()
	b = b.replace(' ', '').lower()
	
	if len(a) != len(b):
		return False
	
	visited = {}
	
	for letter in a:
		if letter in visited:
			visited[letter] += 1
		else:
			visited[letter] = 1
	
	for letter in b:
		if not letter in visited:
			return False
		
		visited[letter] -= 1
		if visited[letter] < 0:
			return False
	
	return True


# solution 2 - sort string
def quickSort(str):
	if len(str) <= 1:
		return str
	
	l = []
	r = []
	p = str[0].lower()
	
	for letter in str[1:]:
		letter = letter.lower()
		if letter > p:
			r.append(letter)
		else:
			l.append(letter)
	
	l = quickSort(l)
	r = quickSort(r)
	
	return l + [p] + r


def isAnagram2(a, b):
	a = quickSort(list(a.replace(' ', '').lower()))
	b = quickSort(list(b.replace(' ', '').lower()))
	return a == b


a = 'public relations'
b = 'crap built on lies'

print(isAnagram1(a, b))
print(isAnagram2(a, b))
