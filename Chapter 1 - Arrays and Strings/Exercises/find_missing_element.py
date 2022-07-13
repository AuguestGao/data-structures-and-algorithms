"""
Given two arrays, B is shuffled version of A with one element removed. Find this element.

example,
find_missing_element([1,2,3,4,5], [3,5,1,2])
// return 4
"""


def find_missing_element(arrA, arrB):
	print(f'method 1 returns: {method_1(arrA, arrB)}')
	print(f'method 2 returns: {method_2(arrA, arrB)}')
	print(f'method 3 returns: {method_3(arrA, arrB)}')


def method_1(arrA, arrB):
	"""
	brute force
	"""
	
	for i in arr_a:
		found = True
		for j in arr_b:
			if i == j:
				found = False
				break
		if found:
			return i
	return None


def method_2(arrA, arrB):
	"""
	sort first - quick sort
	O (n * log n)
	"""
	sortA = mergeSort(arrA)
	sortB = mergeSort(arrB)
	
	for i in range(len(arrB)):
		if sortA[i] != sortB[i]:
			return sortA[i]
	return sortA[-1]
	
	
def mergeSort(arr):
	if len(arr) <= 1:
		return arr
	
	middle = len(arr) // 2
	left = mergeSort(arr[:middle])
	right = mergeSort(arr[middle:])
	
	result = []
	
	while left and right:
		if left[0] < right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	
	return result + left + right


def method_3(arrA, arrB):
	"""
	O(n)
	"""
	dict = {i:True for i in arrB}
	for j in arrA:
		if j not in dict.keys():
			return j
			
	
if __name__ == '__main__':
	arr_a = [1, 2, 3, 4, 5, 6, 7]
	arr_b = [3, 7, 2, 1, 4, 6]
	find_missing_element(arr_a, arr_b)
	