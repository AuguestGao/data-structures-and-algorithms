"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.

time: O(n*log(n)) due to sorting
space: O(n)
"""


class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end
	
	def print_interval(self):
		print("[" + str(self.start) + ", " + str(self.end) + "]", end='')
	

def merge(intervals):
	if len(intervals) < 2: #  0 or 1 intervals
		return intervals
	
	#  sort by interval start
	intervals.sort(key=lambda x: x.start)

	merged_intervals = []
	start = intervals[0].start
	end = intervals[0].end
	
	for interval in intervals[1:]:
		if interval.start <= end:
			# start = min(start, interval.start) #  no need, for start is sorted already
			end = max(end, interval.end)
		else:
			merged_intervals.append(Interval(start, end))
			start = interval.start
			end = interval.end
			
	# add the last interval
	merged_intervals.append(Interval(start, end))
	
	return merged_intervals
	

def main():
	print("Merged intervals: ", end='')
	for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
		i.print_interval()
	print()
	
	print("Merged intervals: ", end='')
	for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
		i.print_interval()
	print()
	
	print("Merged intervals: ", end='')
	for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
		i.print_interval()
	print()


main()
