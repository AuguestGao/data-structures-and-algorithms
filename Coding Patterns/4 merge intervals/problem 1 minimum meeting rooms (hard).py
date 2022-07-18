"""
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
occur in any of the two rooms later.

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
hold all the meetings.

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
"""


def my_solution_2(times):
	times.sort(key=lambda x: x[0])
	rooms = [[times[0]]]
	start, end = 0, 1
	
	for time in times[1:]:
		
		# append time to the room which last meeting does not conflict with current meeting
		i = 0
		
		while i < len(rooms):
			
			last_meeting = rooms[i][-1]
			
			if last_meeting[end] <= time[start]:
				rooms[i].append(time)
				break
			
			i += 1
		
		# all rooms' last meetings conflict with this meeting
		if i == len(rooms):
			rooms.append([time])
			
		return len(rooms)


# time: O(n^2)
# space: O(n)
def my_solution(times):
	times.sort(key=lambda x: x[0])
	rooms = []
	start, end = 0, 1
	
	while times:
		cur = times.pop(0)
		conflicts = []
		meetings = [cur]
		
		while times:
			nxt = times.pop(0)
			
			if nxt[start] < cur[end]:
				conflicts.append(nxt)
			else:
				meetings.append(nxt)
				cur = nxt
				
		times = conflicts[:]
		rooms.append(meetings)

	return len(rooms)


def main():
	inputs = [[[1,4], [2,5], [7,9]], [[6,7], [2,4], [8,12]],[[1,4], [2,3], [3,6]], [[4,5], [2,3], [2,4], [3,5]]]
	for time in inputs:
		res = solution(time)
		print(res)
	
		
main()