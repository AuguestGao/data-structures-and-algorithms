"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def solution(arr, k):
	start, max_length, num_ones_in_window = 0, 0, 0
	
	for end in range(len(arr)):
		if arr[end] == 1:
			num_ones_in_window += 1

		if (end - start + 1) - num_ones_in_window > k:
			if arr[start] == 1:
				num_ones_in_window -= 1
			start += 1
		
		max_length = max(max_length, end - start + 1)
		
	return max_length


def my_solution(arr, k):
	start = 0
	sum_up_to_zero_idx = []
	max_length = 0
	total = 0
	
	for end in range(len(arr)):
		end_num = arr[end]
		
		if not end_num:
			sum_up_to_zero_idx.append((end, total))
		total += end_num
		
		if (end - start + 1) - total > k:
			(idx, up_to_sum) = sum_up_to_zero_idx[len(sum_up_to_zero_idx) - k - 1]
			start, total = idx + 1, total - up_to_sum
			
		max_length = max(max_length, end - start + 1)
		
	return max_length

	
if __name__ == '__main__':
	inputs = [([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), ([1, 0, 0, 0, 0, 0], 2)]
	for arr, k in inputs:
		res = solution(arr, k)
		print(res)