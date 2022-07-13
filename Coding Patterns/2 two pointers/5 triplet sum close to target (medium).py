"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the
target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of
the triplet with the smallest sum.

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

time: O(n^2) i.e. n*log(n) for sort + n^2 for search
space: O(1)
"""


def solution(arr, target):
	arr.sort()
	closest_sum = float('inf')
	
	for i in range(len(arr) - 2):
		closest_sum_pair = get_closest_pair_sum(arr, target - arr[i], i + 1)
		
		if abs(closest_sum_pair + arr[i] - target) < abs(closest_sum - target):
			closest_sum = closest_sum_pair + arr[i]
		
	return closest_sum


def get_closest_pair_sum(arr, target, left):
	right = len(arr) - 1
	closest_sum_pair = float('inf')
	
	while left < right:
		total = arr[left] + arr[right]
		
		if abs(total - target) < abs(closest_sum_pair - target):
			closest_sum_pair = total
		
		if total > target:
			right -= 1
		elif total < target:
			left += 1
		else:
			return 0
		
	return closest_sum_pair
		
	
if __name__ == '__main__':
	inputs = [([-2, 0, 1, 2], 2), ([-3, -1, 1, 2], 1), ([1, 0, 1, 1], 100)]
	for arr, target in inputs:
		res = solution(arr, target)
		print(res)