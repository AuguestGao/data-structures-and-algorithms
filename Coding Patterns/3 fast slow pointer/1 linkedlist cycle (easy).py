"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

time: O(n)
space: O(1)
"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


# solution
def has_cycle(head):
	slow, fast = head, head
	while fast and fast.next:
		slow, fast = slow.next, fast.next.next
		if slow == fast:
			return True
	
	return False


def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	print("LinkedList has cycle: " + str(has_cycle(head)))
	
	head.next.next.next.next.next.next = head.next.next
	print("LinkedList has cycle: " + str(has_cycle(head)))
	
	head.next.next.next.next.next.next = head.next.next.next
	print("LinkedList has cycle: " + str(has_cycle(head)))


main()