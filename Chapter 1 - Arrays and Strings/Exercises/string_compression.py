"""
Given a string, compress the same char with the number representing the amount of the character
chars are case sensitive
can make false compression: "AAB" to "A2B1"

example:
input: 'AAAABBBBCCCCCDDEEEE'
output: 'A2B4C5D2E4'

input: 'AAaaa'
output: 'A2a3'
"""


def method_1(chars):
	
	if len(chars) == 0:
		return ''
	
	if len(chars) == 1:
		return chars + '1'
	
	result = ''
	count = 1
	
	i = 1
	while i < len(chars):
		if chars[i] == chars[i - 1]:
			count += 1
		else:
			result += f'{chars[i-1]}{count}'
			count = 1
		i += 1
	result += f'{chars[i-1]}{count}'
	return result
	

def comp_str(str, answer):
	result1 = method_1(str)
	print(f'method 1 => {result1} vs answer {answer}')


if __name__ == '__main__':
	strs = ['AAAABBBBCCCCCDDEEEE', 'AAaaa', 'AbBC', 'a', '']
	answers = ['A4B4C5D2E4', 'A2a3', 'A1b1B1C1', 'a1', '']
	for i in range(len(strs)):
		comp_str(strs[i], answers[i])
		
