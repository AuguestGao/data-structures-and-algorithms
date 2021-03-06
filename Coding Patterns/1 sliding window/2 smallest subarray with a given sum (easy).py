"""
Given an array of positive numbers and a positive number āSā, find the length of the smallest contiguous subarray whose sum is greater than or equal to āSā. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].+

tag: dynamic window size

time: O(n+n) = O(n)
space: O(1)
"""


def solution(arr, s):

	b, e = 0, 0
	ret = float('inf')
	total = 0

	while e < len(arr):
		if total >= s:
			ret = min(ret, e - b - 1)
			total -= arr[b]
			b += 1
		else:
			total += arr[e]
			e += 1
	return ret


if __name__ == '__main__':
	inputs = [([2, 1, 5, 1, 3, 2],7), ([2, 1, 5, 2, 8], 7), ([3, 4, 1, 1, 6], 8 )]
	for arr, s in inputs:
		res = solution(arr, s)
		print(res)