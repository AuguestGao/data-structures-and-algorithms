"""
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

idea: subtract the element going out of the window and add the new element getting into the window
tag: fixed window size

time: O(N)
space: O(1)
"""


def solution(arr, k):
	if len(arr) <= k:
		return sum(arr)
	
	total = sum(arr[:k])
	ret = total
	
	for i in range(k, len(arr)):
		total = total - arr[i - k] + arr[i]
		ret = max(ret, total)

	return ret
	
	
if __name__ == '__main__':
	inputs = [([2, 1, 5, 1, 3, 2], 3), ([2, 3, 4, 1, 5], 2)]
	for arr, k in inputs:
		res = solution(arr, k)
		print(res)
