"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as
objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three
colors: red, white and blue; and since our input array also consists of three different numbers that is why it is
called Dutch National Flag problem.

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

time: O(n)
space: O(1)
"""


def solution(arr):
	left, idx = 0, 0
	right = len(arr) - 1

	while idx < len(arr):
		if arr[idx] < 1:
			arr[left], arr[idx] = arr[idx], arr[left]
			left += 1
			idx += 1
		elif arr[idx] > 1:
			arr[right], arr[idx] = arr[idx], arr[right]
			right -= 1
		else:
			idx += 1
			
	return arr
	

if __name__ == '__main__':
	inputs = [[1, 0, 2, 1, 0], [2, 2, 0, 1, 2, 0]]
	for arr in inputs:
		res = solution(arr)
		print(res)