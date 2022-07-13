"""
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].

time: O(n)
space: O(1)
"""


def solution(arr, key):
	next_replacement_idx = 0
	next_idx = 0
	
	while next_idx < len(arr):
		if arr[next_idx] != key:
			arr[next_replacement_idx] = arr[next_idx]
			next_replacement_idx += 1
		next_idx += 1
		
	return next_replacement_idx
		
	
if __name__ == '__main__':
	inputs = [([3, 2, 3, 6, 3, 10, 9, 3], 3), ([2, 11, 2, 2, 1], 2)]
	for arr, key in inputs:
		res = solution(arr, key)
		print(res)