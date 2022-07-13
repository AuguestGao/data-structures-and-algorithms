"""
replace spaces with %20 in a string (arr) in place,
the true length of the input string is given (incl. space)
arr has sufficient size
leave the extra space at the end without them are replaced by %20
"""


def urlify(arr, trueLength):
	spaces = 0
	for i in range(trueLength):
		if arr[i] == ' ':
			spaces += 1
	
	total_size = trueLength + 2 * spaces
	
	slow = total_size - 1
	fast = trueLength - 1
	
	
	
	while slow > 0:
		if arr[fast] != ' ':
			arr[slow] = arr[fast]
			slow -= 1
			fast -= 1
		else:
			arr[slow] = '0'
			arr[slow - 1] = '2'
			arr[slow - 2] = '%'
			slow -= 3
			fast -= 1
	return arr


if __name__ == '__main__':
	input_string = "Mr John Smith      "
	trueLength = 13
	s = ''.join(urlify(list(input_string), trueLength))
	print(s)
	
	
	