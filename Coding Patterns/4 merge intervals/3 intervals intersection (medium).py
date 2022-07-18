"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.

time: O(m+n), m,n are lengths for arr1 and arr2
space: O(1)
"""


# solution
def merge(arr1, arr2):
	start, end = 0, 1
	i, j = 0, 0
	intersections = []
	
	while i < len(arr1) and j < len(arr2):
		
		if arr1[i][end] < arr2[j][start]: # arr1 is ahead of arr2 with no overlap
			i += 1
		elif arr2[j][end] < arr1[i][start]: # arr1 is behind arr2 with no overlap
			j += 1
		else:
			intersect_start = max(arr1[i][start], arr2[j][start])
			intersect_end = min(arr1[i][end], arr2[j][end])
			intersections.append([intersect_start, intersect_end])
			if arr1[i][end] < arr2[j][end]: # advance arr1 for arr1 end is smaller
				i += 1
			elif arr1[i][end] > arr2[j][end]: # advance arr2 for arr2 end is smaller
				j += 1
			else: # advance both
				i += 1
				j += 1

	return intersections
	

def main():
	print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
	print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()