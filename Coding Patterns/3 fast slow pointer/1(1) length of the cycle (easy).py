"""
Given the head of a LinkedList with a cycle, find the length of the cycle.

time: O(n)
space: O(1)
"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


# solution
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
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()