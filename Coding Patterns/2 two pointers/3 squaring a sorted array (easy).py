"""
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

time: O(n)
space: O(n)
"""


def solution(arr):
	total_nums = len(arr)
	squared = [0] * total_nums
	left, right = 0, total_nums - 1
	fill_index = total_nums - 1
	
	while left <= right:
		left_square = arr[left] ** 2
		right_square = arr[right] ** 2
		
		if left_square > right_square:
			squared[fill_index] = left_square
			left += 1
		else:
			squared[fill_index] = right_square
			right -= 1
		fill_index -= 1
	
	return squared
	

if __name__ == '__main__':
	inputs = [[-2, -1, 0, 2, 3], [-3, -1, 0, 1, 2]]
	for arr in inputs:
		res = solution(arr)
		print(res)
