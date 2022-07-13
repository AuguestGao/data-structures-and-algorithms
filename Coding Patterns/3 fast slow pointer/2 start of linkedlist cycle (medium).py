"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

time: O(n)
space: O(1)
"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def print_list(self):
	temp = self
	while temp is not None:
		print(temp.value, end='')
		temp = temp.next
	print()


def find_cycle_start(head):
	cycle_length = find_cycle_length(head)
	slow, fast = head, head
	
	for step in range(cycle_length):
		fast = fast.next
		
	while slow != fast:
		slow = slow.next
		fast = fast.next
		
	return slow


def find_cycle_length(head):
	slow, fast = head.next, head.next.next
	count = 1
	
	while slow != fast:
		count += 1
		slow = slow.next
		fast = fast.next.next
	
	return count

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
	
