"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].


time: O(n)
space: O(n)
"""


def solution(intervals, new_interval):
	merged = []
	i = 0
	start, end = 0, 1
	
	# skip intervals before new_interval
	while i < len(intervals) and intervals[i][end] < new_interval[start]:
		merged.append(intervals[i])
		i += 1
		
	# merge intervals
	while i < len(intervals) and intervals[i][start] <= new_interval[end]:
		new_interval[start] = min(intervals[i][start], new_interval[start])
		new_interval[end] = max(intervals[i][end], new_interval[end])
		i += 1
	merged.append(new_interval)
	
	# add all remaining intervals
	while i < len(intervals):
		merged.append(intervals[i])
		i += 1
		
	return merged
	

def main():
	print("Intervals after inserting the new interval: " + str(solution([[1, 3], [5, 7], [8, 12]], [4, 6])))
	print("Intervals after inserting the new interval: " + str(solution([[1, 3], [5, 7], [8, 12]], [4, 10])))
	print("Intervals after inserting the new interval: " + str(solution([[2, 3], [5, 7]], [1, 4])))


main()