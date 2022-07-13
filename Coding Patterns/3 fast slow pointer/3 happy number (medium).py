"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
they will be stuck in a cycle of numbers which does not include ‘1’.
"""


# time: O(log(n))
# space: O(1)
def solution(num):
	slow, fast = num, num
	
	while fast != 1:
		slow = get_sum(slow)
		fast = get_sum(get_sum(fast))
		
		if slow == fast:
			return False
		
	return True
	
	
# time: O(log(n)), n is the number
# space: O(n),
def my_solution(num):
	seen = {}
	
	while num != 1:
		if num in seen:
			return False
		
		seen[num] = True
		num = get_sum(num)
		
	return True
	
	
def get_sum(num):
	new_num = 0
	while num:
		digit = num % 10
		new_num += digit ** 2
		num //= 10
	
	return new_num


def main():
	inputs = [23, 12]
	for num in inputs:
		res = solution(num)
		print(res)
		

main()
