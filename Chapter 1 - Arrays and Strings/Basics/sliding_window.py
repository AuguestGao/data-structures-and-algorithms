"""
Given an array of integers of size ‘n’.
calculate the maximum sum of ‘k’ consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39 by {4, 2, 10, 23}

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
"""


def sliding(arr, k):
	n = len(arr)
	if n < k:
		return 'impossible'
	if n == k:
		return arr
	
	max_sum = float('-inf')
	for i in range(n - k + 1):
		curr_sum = 0
		for j in range(k):
			curr_sum += arr[i + j]
		max_sum = max(curr_sum, max_sum)
	return max_sum

if __name__ == '__main__':
	arr = [100, 200, 300, 400]
	k = 2
	print(sliding(arr, k))