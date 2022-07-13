"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

# an non-optimal solution is to use one pointer to loop through the array and use binary search to fing the needed number in the rest of the array


def solution(arr, target):
	left, right = 0, len(arr) - 1
	
	while left < right:
		curr_sum = arr[left] + arr[right]
		if curr_sum > target:
			right -= 1
		elif curr_sum < target:
			left += 1
		else:
			return [left, right]
	return [-1, -1]


if __name__ == '__main__':
	inputs = [([1, 2, 3, 4, 6], 6), ([2, 5, 9, 11], 11)]
	for arr, target in inputs:
		res = solution(arr, target)
		print(res)


