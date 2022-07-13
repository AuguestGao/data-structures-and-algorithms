"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

time: O(n)
space: O(1)
"""


def solution(arr):
	next_non_dup_idx = 1
	next_idx = 1
	
	while next_idx < len(arr):
		if arr[next_non_dup_idx - 1] != arr[next_idx]:
			next_non_dup_idx, next_idx = next_idx, next_idx + 1
			arr[next_non_dup_idx] = arr[next_idx]
		next_idx += 1
	return next_non_dup_idx
		
	
if __name__ == '__main__':
	inputs = [[2, 3, 3, 3, 6, 9, 9], [2, 2, 2, 11]]
	for arr in inputs:
		res = solution(arr)
		print(res)