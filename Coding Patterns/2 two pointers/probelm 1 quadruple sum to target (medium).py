"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to
the target number.

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

time: O(n^3) i.e. O(n*log(n)) for sorting and O(n^3) for getting quadruplets
space: O(n)
"""


def solution(arr, target):
	arr.sort()
	quadruples = []
	for i in range(len(arr) - 3):
		if i > 0 and arr[i] == arr[i - 1]:  # skip duplicated i
			continue
		for j in range(i + 1, len(arr) - 2):
			if j > i + 1 and arr[j] == arr[j - 1]:  # skip duplicated j
				continue
			search_pair(arr, target - arr[i] - arr[j], i, j, quadruples)
	
	return quadruples


def search_pair(arr, pair_target, i, j, quadruples):
	left = j + 1
	right = len(arr) - 1
	
	while left < right:
		pair_sum = arr[left] + arr[right]
		if pair_sum > pair_target:
			right -= 1
		elif pair_sum < pair_target:
			left += 1
		else:
			quadruples.append([arr[i], arr[j], arr[left], arr[right]])
			left += 1
			right -= 1
			while left < right and arr[left] == arr[left - 1]:
				left += 1
			while left < right and arr[right] == arr[right + 1]:
				right -= 1
	

if __name__ == '__main__':
	inputs = [([4, 1, 1, 2, -1, 1, -3], 1), ([2, 0, -1, 1, -2, 2], 2)]
	for arr, target in inputs:
		res = solution(arr, target)
		print(res)