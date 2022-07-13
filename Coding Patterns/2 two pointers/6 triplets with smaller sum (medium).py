"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[
k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


time: O(n^2) i.e. n*long(n) for sorting + n^3 for searching (n^2 for search pair)
space: O(1)
"""


def solution(arr, target):
	arr.sort()
	triplets_count = 0
	
	for i in range(len(arr) - 2):
		pair_target = target - arr[i]
		triplets_count += find_pairs(arr, pair_target, i + 1)
		
	return triplets_count


def find_pairs(arr, target, left):
	right = len(arr) - 1
	count = 0
	
	while left < right:
		if arr[left] + arr[right] < target:
			count += right - left
			left += 1
		else:
			right -= 1
	return count

	
if __name__ == '__main__':
	inputs = [([-1, 0, 2, 3], 3), ([-1, 4, 2, 1, 3], 5)]
	for arr, target in inputs:
		res = solution(arr, target)
		print(res)