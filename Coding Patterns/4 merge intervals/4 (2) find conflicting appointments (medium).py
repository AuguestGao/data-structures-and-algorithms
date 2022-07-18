"""
Given a list of appointments, find all the conflicting appointments.

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output:
[4,5] and [3,6] conflict.
[3,6] and [5,7] conflict.
"""


def solution(appointments):
	appointments.sort(key=lambda x: x[0])
	start, end = 0, 1
	conflicts = []
	
	cur = 0
	nxt = 1
	
	while nxt < len(appointments):
		
		while nxt < len(appointments) and appointments[nxt][start] < appointments[cur][end]:
			conflicts.append([appointments[cur], appointments[nxt]])
			nxt += 1
			
		cur += 1
		nxt = cur + 1
		
	return conflicts
	
	
def main():
	res = solution([[4,5], [2,3], [3,6], [5,7], [7,8]])
	print(res)
	
main()