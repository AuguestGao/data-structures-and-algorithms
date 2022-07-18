"""Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointment

time: O(n*log(n))
space: O(N)
"""


def solution(appointments):
	appointments.sort(key=lambda x: x[0])
	
	start, end = 0, 1
	prev_end = appointments[0][end]
	
	for i in range(1, len(appointments)):
		
		if appointments[i][start] < prev_end:
			return False
		
		prev_end = appointments[i][end]

	return True
	
	
def main():
	inputs = [[[1,4], [2,5], [7,9]],  [[6,7], [2,4], [8,12]], [[1,4], [2,6], [3,5]]]
	for appointments in inputs:
		res = solution(appointments)
		print(res)
		
		
main()