"""
Given two strings, check if one is a permutation of the other

"""


def method_1(str1, str2):
	"""
	use dictionary to record str1 chars and their amounts
	traverse str2 and reduce char's amount from the dictionary
	if there is no char or char's amount == 0 return False
	otherwise, return True
	"""
	if len(str1) != len(str2):
		return False
	
	record = {}
	
	for i in str1:
		if i not in record.keys():
			record[i] = 1
		else:
			record[i] += 1
	
	for j in str2:
		if j not in record.keys():
			return False
		elif record[j] == 0:
			return False
		else:
			record[j] -= 1
	return True
	
	
def method_2(str1, str2):
	"""
	O (n * log(n))
	"""
	if len(str1) != len(str2):
		return False
	
	str1 = sort_str(str1)
	str2 = sort_str(str2)
	
	return str1 == str2
	
	
def sort_str(s):
	return ''.join(sorted(list(s)))


def method_3(str1, str2):
	"""
	assume ascii chars
	use char ascii number as index to count its amount
	"""
	if len(str1) != len(str2):
		return False
	
	arr1 = [0] * 128
	arr2 = [0] * 128
	
	for i in range(len(str1)):
		c1 = ord(str1[i])
		c2 = ord(str2[i])
		arr1[c1] += 1
		arr2[c2] += 1
	
	return arr1 == arr2
	

def check_permutation(str1, str2):
	print(f'method 1 => {method_1(str1, str2)}')
	print(f'method 2 => {method_2(str1, str2)}')
	print(f'method 3 => {method_3(str1, str2)}')
	
	
if __name__ == '__main__':
	str1s = ['a', '', 'abvv b', 'ab']
	str2s = ['a', '', 'bvvba ', 'bv']
	
	for i in range(len(str1s)):
		check_permutation(str1s[i], str2s[i])
		
