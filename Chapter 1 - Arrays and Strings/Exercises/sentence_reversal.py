"""
Given a string, reverse all the words (not char)
remove leading and trailing whitespaces

example:
input: 'this is the best'
output: 'best the is This`
"""
import string


def method_1(str):
	# avoid to use in interview
	return  ' '.join(str.strip().split(' ')[::-1])
	
	
def method_2(str):
	result = ''
	space = ''  # prevent duplicated spaces
	word = ''
	for i in str:
		
		if i.lower() in string.ascii_lowercase:
			space = ''
			word += i
		else:
			if ' ' not in space:
				space += ' '
				result = word + ' ' + result
			word = ''
	return result
	
	
def rev_sent(str):
	result1 = method_1(str)
	result2 = method_2(str)
	
	print(f'method 1 =>{result1}')
	print(f'method 2 =>{result2}')


if __name__ == '__main__':
	strs = [' this is the best  ', ' hello John how are you ']
	for str in strs:
		rev_sent(str)
