"""
given a string, return True if all chars are unique.

example
input: 'abcv'
output: True

input: 'abbc'
output: False
"""
import string


def method_1(str):
	dict = {char: True for char in string.ascii_letters}
	for c in str:
		if dict[c] == True:
			dict[c] = False
		else:
			return False
	return True

def method_2(str):
	visited = set()
	for char in str:
		if char not in visited:
			visited.add(char)
		else:
			return False
	return True


def uniq_char(str, answer):
	print(f'method 1 => {method_1(str)} vs answer {answer}')
	print(f'method 2 => {method_2(str)} vs answer {answer}')


if __name__ == '__main__':
	strs = ['abvc', 'abca', 'aa', 'b']
	answers = [True, False, False, True]
	for i in range(len(strs)):
		uniq_char(strs[i], answers[i])
	
	