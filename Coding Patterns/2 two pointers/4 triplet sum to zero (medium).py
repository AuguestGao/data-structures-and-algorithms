"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""


def solution(arr):
	arr.sort()
	triplets = []
	
	for i in range(len(arr) - 2):
		if i > 0 and arr[i] == arr[i - 1]:  # skip duplicate number
			continue
		get_pair(arr, -arr[i], i + 1, triplets)
	
	return triplets


def get_pair(arr, target, left, triplets):
	right = len(arr) - 1
	
	while left < right:
		total = arr[left] + arr[right]
		
		if total == target:
			triplets.append([-target, arr[left], arr[right]])
			left += 1
			right -= 1
			
			while left < right and arr[left - 1] == arr[left]:
				left += 1
			while left < right and arr[right + 1] == arr[right]:
				right -= 1
		elif total > target:
			right -= 1
		else:
			left += 1
			
		
def my_solution(arr):
	
	triplets = set()
	
	for left in range(len(arr) - 2):
		left_num = arr[left]
		seen = {} # number: True
		
		for right in range(left + 1, len(arr)):
			right_num = arr[right]
			need = 0 - left_num - right_num
			
			if need in seen:
				triplets.add((arr[left], need, arr[right]))
			else:
				seen[right_num] = True
	
	return triplets


if __name__ == '__main__':
	inputs = [[-3, 0, 1, 2, -1, 1, -2], [-5, 2, -1, -2, 3]]
	for arr in inputs:
		res = solution(arr)
		print(res)